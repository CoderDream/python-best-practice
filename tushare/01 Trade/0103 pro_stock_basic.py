import tushare as ts

ts.set_token('7483f126babf5e250781d90a96d28f057961392f482e10b98ef2914c')

pro = ts.pro_api()


data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
print(data)
