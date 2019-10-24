import tushare as ts
import openpyxl

df = ts.get_hist_data('000875')
#直接保存
df.to_excel('xlsx/000875.xlsx')

#设定数据位置（从第3行，第6列开始插入数据）
df.to_excel('xlsx/000875.xlsx', startrow=2,startcol=5)
