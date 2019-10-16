# 查询集合中所有数据
# find() 方法可以查询集合中的所有数据，类似 SQL 中的 SELECT * 操作。

# 以下实例查找 sites 集合中的所有数据：

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]

for x in mycol.find():
    print(x)
