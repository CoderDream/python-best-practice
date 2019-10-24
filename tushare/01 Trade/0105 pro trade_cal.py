import tushare as ts

ts.set_token('7483f126babf5e250781d90a96d28f057961392f482e10b98ef2914c')

pro = ts.pro_api()
# 获取各大交易所交易日历数据,默认提取的是上交所
data = pro.query('trade_cal', start_date='20180101', end_date='20181231')
print(data)
