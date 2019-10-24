import tushare as ts

df = ts.get_hist_data('600848')  # 一次性获取全部日k线数据
t = df.head(10)
# print(t)

df2 = ts.get_hist_data('600848', start='2010-01-01', end='2017-03-31')
t2 = df2.head(10)
print(t2)
