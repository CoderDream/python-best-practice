import tushare as ts

# 暂停上市股票列表¶
# 获取被暂停上市的股票列表，数据从上交所获取，目前只有在上海证券交易所交易被终止的股票。
#
# 返回值说明：
#
# code：股票代码
# name：股票名称
# oDate:上市日期
# tDate:暂停上市日期

df = ts.get_suspended()
print(df)

# Expecting value: line 1 column 1 (char 0)
# None
