import pymongo
import tushare as ts

t = ts.get_today_all()
print(t)

# UnicodeDecodeError: 'gbk' codec can't decode byte 0xab in position 2258: illegal multibyte sequence
