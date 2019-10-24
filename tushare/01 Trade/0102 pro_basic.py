import tushare as ts

ts.set_token('7483f126babf5e250781d90a96d28f057961392f482e10b98ef2914c')

pro = ts.pro_api()


df = pro.trade_cal(exchange='', start_date='20180901', end_date='20181001', fields='exchange,cal_date,is_open,pretrade_date', is_open='0')

print(df)

