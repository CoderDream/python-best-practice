import tushare as ts
df = ts.get_today_ticks('601333')  #当天历史分笔
t = df.head(10)
print(t)

# import tushare as ts
df = ts.get_tick_data('600848', date='2018-12-12', src='tt')
df.head(10)
