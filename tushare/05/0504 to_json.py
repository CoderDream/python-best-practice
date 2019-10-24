import tushare as ts

df = ts.get_hist_data('000875')
df.to_json('json/000875.json',orient='records')

#或者直接使用
print(df.to_json(orient='records'))