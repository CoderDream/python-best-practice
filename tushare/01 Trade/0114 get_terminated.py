import tushare as ts

df = ts.get_terminated()
print(df)

df = ts.get_suspended()
print(df)
