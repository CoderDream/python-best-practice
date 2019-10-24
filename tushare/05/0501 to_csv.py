import tushare as ts

df = ts.get_hist_data('000875')
# 直接保存
df.to_csv('csv/000875_1.csv')

# 选择保存
df.to_csv('csv/000875_2.csv', columns=['open', 'high', 'low', 'close'])
