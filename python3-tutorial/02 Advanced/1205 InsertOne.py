# 返回 _id 字段
# insert_one() 方法返回 InsertOneResult 对象，该对象包含 inserted_id 属性，它是插入文档的 id 值。

import pymongo

myclient = pymongo.MongoClient('mongodb://chenqingwh.uicp.net:37017/')
mydb = myclient["quant_01"]
mycol = mydb["sites"]

mydict = {"name": "Google", "alexa": "1", "url": "https://www.google.com"}

x = mycol.insert_one(mydict)

print(x.inserted_id)
