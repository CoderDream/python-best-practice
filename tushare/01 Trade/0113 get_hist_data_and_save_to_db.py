import tushare as ts
import pymongo
import json

conn = pymongo.MongoClient("mongodb://localhost:27017/")

df = ts.get_hist_data('000651')  # 一次性获取全部日k线数据
conn.db.histdata.insert_many(json.loads(df.to_json(orient='records')))
