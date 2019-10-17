# 查询指定字段的数据
# 我们可以使用 find() 方法来查询指定字段的数据，将要返回的字段对应值设置为 1。

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]

for x in mycol.find({}, {"_id": 0, "name": 1, "alexa": 1}):
    print(x)

# 除了 _id 你不能在一个对象中同时指定 0 和 1，如果你设置了一个字段为 0，则其他都为 1，反之亦然。

print('-------------------------------------')
# 以下实例除了 alexa 字段外，其他都返回：

for x in mycol.find({}, {"alexa": 0}):
    print(x)
