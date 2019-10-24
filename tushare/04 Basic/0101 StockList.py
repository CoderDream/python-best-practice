import tushare as ts

df = ts.get_stock_basics()
# print(tickerList)

# for ticker in df:
#     print(ticker)
    # print(ticker['code'])

# print(df)
record4 = df.head(4)
print(record4)

datacount = 0
for stockIndex in df.index:
    stock = dict(df.loc[stockIndex])
    # stock["_id"] = stock['code'] + stock['date']
    # print(stock)
    datacount += 1
    print(stockIndex)
    # print(stock['name'])

print(datacount)
