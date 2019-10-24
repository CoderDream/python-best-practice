import tushare as ts

# 上证50成份股
# 获取上证50成份股
#
# 返回值说明：
#
# code：股票代码
# name：股票名称

df = ts.get_sz50s()
print(df)

# read_excel() got an unexpected keyword argument `parse_cols`
# None



