import pymongo
import tushare as ts
import json


class TradeClass:
    def __init__(self):
        self.DB_CONN = pymongo.MongoClient('mongodb://chenqingwh.uicp.net:37017')['quant_01']
        self.trade = self.DB_CONN["trade"]

    def save_one_trade_from_tushare(self, ticker_id, trade_day):
        # cur = ts.get_tick_data(ticker_id, date=trade_day)
        df = ts.get_tick_data('603160', date='2018-10-15')

        print(df)
        # array = list(cur)
        # print(type(array))
        # print(len(array))

        return df


if __name__ == '__main__':
    # print(sys.argv)
    trade_instance = TradeClass()
    code = '603160'
    ticker_dfcf_set = trade_instance.save_one_trade_from_tushare(code, '2018-10-15')
