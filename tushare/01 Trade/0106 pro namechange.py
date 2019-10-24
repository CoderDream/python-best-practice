import tushare as ts

ts.set_token('7483f126babf5e250781d90a96d28f057961392f482e10b98ef2914c')

pro = ts.pro_api()
# 历史名称变更记录
df = pro.namechange(ts_code='600848.SH', fields='ts_code,name,start_date,end_date,change_reason')
print(df)


df = ts.get_tick_data('600848',date='2018-12-12',src='tt')
print(df.head(10))
