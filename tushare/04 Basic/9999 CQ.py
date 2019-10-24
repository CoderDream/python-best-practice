import tushare as ts
from datetime import datetime
import threading
from pymongo import MongoClient
import sys
from pymongo import UpdateOne

import queue
from pymongo import InsertOne


class AsyncTask(threading.Thread):
    def __init__(self, start, end, collection):
        threading.Thread.__init__(self)
        self.start_date = start
        self.end_date = end
        self.collection = collection

    def run(self):
        while len(HistoryDataManager.need_get_pool) > 0 and AsyncTask.index < AsyncTask.maxTime:
            AsyncTask.threadLock.acquire()
            AsyncTask.index += 1
            idx = AsyncTask.index
            stock_code = HistoryDataManager.need_get_pool.pop(0)
            AsyncTask.threadLock.release()
            start_time = datetime.utcnow()
            try:
                stocks = ts.get_k_data(stock_code, index=False, start=self.start_date, end=self.end_date)
                datacount = 0
                for stockIndex in stocks.index:
                    stock = dict(stocks.loc[stockIndex])
                    stock["_id"] = stock['code'] + stock['date']
                    stock["index"] = False
                    self.collection.save(stock)
                    datacount += 1
                # self.save_data(stock_code, stocks, self.collection)
                end_time = datetime.utcnow()
                end_time_str = end_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                timest = end_time - start_time
                print(
                    "%s--%d--%d:%d--------处理数据:%s 完毕,记录数:%d。" % (
                        end_time_str, idx, timest.seconds, timest.microseconds, stock_code, datacount))
            except Exception as err:
                AsyncTask.threadLock.acquire()
                AsyncTask.index = AsyncTask.maxTime
                HistoryDataManager.need_get_pool.append(stock_code)
                AsyncTask.threadLock.release()
                end_time = datetime.utcnow()
                end_time_str = end_time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                timest = end_time - start_time
                print(
                    "%s--%d--%d:%d--------处理数据:%s 失败!!!" % (
                        end_time_str, idx, timest.seconds, timest.microseconds, stock_code))
                print(err)

    def save_data(self, code, df_daily, collection, extra_fields=None):
        """
        将从网上抓取的数据保存到本地MongoDB中

        :param code: 股票代码
        :param df_daily: 包含日线数据的DataFrame
        :param collection: 要保存的数据集
        :param extra_fields: 除了K线数据中保存的字段，需要额外保存的字段
        """

        # 数据更新的请求列表
        update_requests = []

        # 将DataFrame中的行情数据，生成更新数据的请求
        for df_index in df_daily.index:
            # 将DataFrame中的一行数据转dict
            doc = dict(df_daily.loc[df_index])
            # 设置股票代码
            doc['code'] = code
            doc["index"] = False
            # 如果指定了其他字段，则更新dict
            if extra_fields is not None:
                doc.update(extra_fields)

            # 生成一条数据库的更新请求
            # 注意：
            # 需要在code、date、index三个字段上增加索引，否则随着数据量的增加，
            # 写入速度会变慢，创建索引的命令式：
            # db.daily.createIndex({'code':1,'date':1,'index':1})
            update_requests.append(
                UpdateOne(
                    {'code': doc['code'], 'date': doc['date'], 'index': doc['index']},
                    {'$set': doc},
                    upsert=True)
            )

        # 如果写入的请求列表不为空，则保存都数据库中
        if len(update_requests) > 0:
            # 批量写入到数据库中，批量写入可以降低网络IO，提高速度
            update_result = collection.bulk_write(update_requests, ordered=False)
            print('保存日线数据，代码： %s, 插入：%4d条, 更新：%4d条' %
                  (code, update_result.upserted_count, update_result.modified_count),
                  flush=True)

    @classmethod
    def bigin(cls, pool_size, max_time, start, end, collection):
        cls.threadLock = threading.Lock()
        cls.index = 0
        cls.maxTime = max_time
        cls.pool = []
        l = 0
        l_time_s = datetime.utcnow()
        l_time_str = l_time_s.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        print(
            "%s----------开始处理数据-线程池大小:%d--处理数量:%d--开始日期:%s--结束日期:%s" % (
                l_time_str, pool_size, max_time, start, end))
        while l < pool_size:
            task = AsyncTask(start, end, collection)
            cls.pool.append(task)
            task.start()
            l += 1
        for t in cls.pool:
            t.join()
        l_time_e = datetime.utcnow()
        l_time_str = l_time_e.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        timest = l_time_e - l_time_s
        print(
            "%s-----%d:%d-----完成处理数据----------------开始日期:%s--结束日期:%s" % (
                l_time_str, timest.seconds, timest.microseconds, start, end))


class HistoryDataManager:
    def __init__(self):
        # self.DB_CONN = MongoClient('mongodb://chenqingwh.uicp.net:37017')['quant_01']
        self.DB_CONN = MongoClient('mongodb://192.168.0.164:27017')['quant_01']
        self.stocksCLLS = self.DB_CONN["stocks"]
        self.needProcessPool = self.DB_CONN["history_task_pool"]
        self.stockdalily = self.DB_CONN["stock_caily"]

    def init_load_dir(self, is_reload=False):
        history_daily = self.needProcessPool.find({"name": "HistoryDaily"})
        history_daily_list = list(history_daily)
        if history_daily_list == [] or is_reload:
            data = self.stocksCLLS.find({})
            HistoryDataManager.need_get_pool = []
            for x in data:
                HistoryDataManager.need_get_pool.append(x["code"])
            if history_daily_list == []:
                self.needProcessPool.insert({"name": "HistoryDaily", "list": HistoryDataManager.need_get_pool})
            else:
                self.save_load_dir(HistoryDataManager.need_get_pool)
        else:
            HistoryDataManager.need_get_pool = history_daily_list[0]["list"]

    def save_load_dir(self, data):
        self.needProcessPool.update({"name": "HistoryDaily"},
                                    {"name": "HistoryDaily", "list": data})

    def load_daily_data(self, pool_size, count, start, end):
        AsyncTask.bigin(pool_size, count, start, end, self.stockdalily)


HistoryDataManager.failed_pool = []
if __name__ == '__main__':
    # print(sys.argv)
    hdManager = HistoryDataManager()
    if sys.argv[5] == "-r":
        hdManager.init_load_dir(True)
    else:
        hdManager.init_load_dir(False)
    hdManager.load_daily_data(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4])
    hdManager.save_load_dir(HistoryDataManager.need_get_pool)
    print("保存队列完毕.-------------------------------------")
    # print(HistoryDataManager.need_get_pool)
    # print(len(HistoryDataManager.need_get_pool))

# print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
# print(ts.get_stock_basics())
# print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
# ts.get_hist_data('600848')
