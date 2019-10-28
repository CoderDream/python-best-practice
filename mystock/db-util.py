# Requires pymongo 3.6.0+
from pymongo import MongoClient

# client = MongoClient("mongodb://chenqingwh.uicp.net:37017/")
# database = client["quant_01"]
# collection = database["gps"]

# Created with Studio 3T, the IDE for MongoDB - https://studio3t.com/

# query = {"local":"sh"}

# query = {"id": "000016"}
# 国债回购（席位托管方式）
# query = {"id": {"$regex": "^201"}, "local": "sh"}

# query = {"id": {"$regex": "^600"}, "local": "sh"}
# query = {"id": {"$regex": "^60[0-1]"}, "local": "sh"}


# query = {"id": {"$regex": "^70[0-1]"}, "local": "sh"}


# query = {"id": {"$regex": "^03"}, "local": "sz"}


# query = {"id": {"$regex": "^78"}, "local": "sh"}
#
# # cursor = collection.find(query, skip=4948, limit=50)
# cursor = collection.find(query)
# try:
#     for doc in cursor:
#         print(doc)
# finally:
#     client.close()


class StockDataManager:
    def __init__(self):
        self.DB_CONN = MongoClient('mongodb://chenqingwh.uicp.net:37017')['quant_01']
        # self.DB_CONN = MongoClient('mongodb://192.168.0.164:27017')['quant_01']
        self.gps = self.DB_CONN["gps"]
        self.code_type = self.DB_CONN["code_type"]

    def load_stock(self, stock_code, local):
        query = {"id": stock_code, "local": local}

        # cursor = collection.find(query, skip=4948, limit=50)
        cursor = self.gps.find(query)
        stocks = []
        for doc in cursor:
            # print(doc)
            stocks.append(doc)

        return stocks

    def load_stock_by_code_type(self, stock_code, local):
        # query = {"id": stock_code, "local": local}

        query = {"id": {"$regex": "^" + stock_code}, "local": local}

        # cursor = collection.find(query, skip=4948, limit=50)
        cursor = self.gps.find(query)
        stocks = []
        for doc in cursor:
            # print(doc)
            stocks.append(doc)

        return stocks

    def load_stock_list(self, local):
        stocks = []
        # query = {"id": {"$regex": "^60[0-1]"}, "local": local}

        temp_code_type_list = self.load_code_type(local)
        for temp in temp_code_type_list:
            temp_stocks_list = self.load_stock_by_code_type(temp, local)
            for doc in temp_stocks_list:
                # print(doc)
                stocks.append(doc)
        return stocks

    def load_code_type(self, local):
        query = {"type": 1, "local": local}

        # cursor = collection.find(query, skip=4948, limit=50)
        cursor = self.code_type.find(query)
        code_types = []
        for doc in cursor:
            # print(doc)
            #code_types.append(doc)
            code_types.append(doc['prefix'])

        return code_types


if __name__ == '__main__':
    stock_data_manager = StockDataManager()
    # stock_list = stock_data_manager.load_stock('sh')
    # print(len(stock_list))

    # code_type_list = stock_data_manager.load_code_type('sh')
    # print(len(code_type_list))
    # print(code_type_list)

    print(len(stock_data_manager.load_stock_list('sh')))
    # print(stock_data_manager.load_stock_list('sh'))

    # print(stock_data_manager.load_stock_by_code_type('600', 'sh'))
