import tushare as ts
# df = ts.get_tick_data('600848', date='2018-01-09')
# df.head(10)
# df = ts.get_today_ticks('601333')  #当天历史分笔
# df.head(10)
# import tushare as ts
df = ts.get_realtime_quotes('000581') #Single stock symbol
df[['code','name','price','bid','ask','volume','amount','time']]
#symbols from a list
ts.get_realtime_quotes(['600848','000980','000981'])
#from a Series
ts.get_realtime_quotes(df['code'].tail(10))  #一次获取10个股票的实时分笔数据