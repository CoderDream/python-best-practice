import tushare as ts

# 终止上市股票列表¶
# 获取已经被终止上市的股票列表，数据从上交所获取，目前只有在上海证券交易所交易被终止的股票。
#
# 返回值说明：
#
# code：股票代码
# name：股票名称
# oDate:上市日期
# tDate:终止上市日期

df = ts.get_terminated()
print(df)

# Expecting value: line 1 column 1 (char 0)
# None

