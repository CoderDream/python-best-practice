import tushare as ts
import pymongo
import json

conn = pymongo.MongoClient("mongodb://localhost:27017/") # pymongo.Connection('127.0.0.1', port=27017)
df = ts.get_index() #ts.get_tick_data('600848', date='2014-12-22')

conn.db.tickdata.insert_many(json.loads(df.to_json(orient='records')))
