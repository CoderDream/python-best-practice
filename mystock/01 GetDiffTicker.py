import pymongo


class TickerClass:
    def __init__(self):
        self.DB_CONN = pymongo.MongoClient('mongodb://chenqingwh.uicp.net:37017')['quant_01']
        self.gps = self.DB_CONN["gps"]
        self.stocks = self.DB_CONN["stocks"]

    def find_ticker_list_from_tushare(self):
        cur = self.stocks.find({}, {"_id": 0, "code": 1})

        array = list(cur)
        # print(type(array))
        # print(len(array))
        return array

    def find_ticker_id_set_from_tushare(self):
        array = self.find_ticker_list_from_tushare()
        id_set = set()
        for ticker in array:
            id_set.add(ticker['code'])
        return id_set

    def find_ticker_from_dfcf(self, ticker_id):
        cur = self.gps.find({"id": ticker_id})

        array = list(cur)
        # print(type(array))
        # print(len(array))
        return array

    def find_ticker_list_from_dfcf(self):
        cur = self.gps.find({}, {"_id": 0, "id": 1, "name": 1})

        array = list(cur)
        # print(type(array))
        # print(len(array))
        return array

    def find_ticker_id_set_from_dfcf(self):
        array = self.find_ticker_list_from_dfcf()
        id_set = set()
        for ticker in array:
            id_set.add(ticker['id'])
        return id_set


if __name__ == '__main__':
    # print(sys.argv)
    tickerClass = TickerClass()
    ticker_dfcf_set = tickerClass.find_ticker_id_set_from_dfcf()
    ticker_tushare_set = tickerClass.find_ticker_id_set_from_tushare()
    stock_set_diff = ticker_dfcf_set.difference(ticker_tushare_set)
    print(len(stock_set_diff))

    ticker_id_list = []
    for ticker_id in stock_set_diff:
        ticker_id_list.append(ticker_id)

    ticker_id_list.sort()

    for ticker_id in ticker_id_list:
        # print(ticker_id)
        ticker_one = tickerClass.find_ticker_from_dfcf(ticker_id)
        str = ticker_one[0]['id'] + ":" + ticker_one[0]['name']
        print(str)

    # ticker_one = tickerClass.find_ticker_from_dfcf("000003")
    # ticker_one = tickerClass.find_ticker_from_dfcf("900957")
    #
    # print(ticker_one)
