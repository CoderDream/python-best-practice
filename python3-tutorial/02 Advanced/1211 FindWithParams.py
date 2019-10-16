# 根据指定条件查询
# 我们可以在 find() 中设置参数来过滤数据。

# 以下实例查找 name 字段为 "RUNOOB" 的数据：

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["site3"]

myquery = {"name": "RUNOOB"}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)
