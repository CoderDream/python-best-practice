# 插入多个文档
# 集合中插入多个文档使用 insert_many() 方法，该方法的第一参数是字典列表。
# !/usr/bin/python3

import pymongo
from pymongo import InsertOne
#myclient = pymongo.MongoClient('mongodb://chenqingwh.uicp.net:37017')
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]

mylist = [
    {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
    {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
    {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
    {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
    {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
]
# buffer=[]
# for item in mylist:
#     buffer.append(InsertOne(item))
# mycol.bulk_write(buffer, ordered=False)
x = mycol.insert_many(mylist)

# 输出插入的所有文档对应的 _id 值
print(x.inserted_ids)
