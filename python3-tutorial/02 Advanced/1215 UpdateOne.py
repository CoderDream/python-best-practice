# 我们可以在 MongoDB 中使用 update_one() 方法修改文档中的记录。该方法第一个参数为查询的条件，第二个参数为要修改的字段。

# 如果查找到的匹配数据多余一条，则只会修改第一条。

# 以下实例将 alexa 字段的值 100 改为 123:

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]

myquery = {"alexa": "100"}
newvalues = {"$set": {"alexa": "123"}}

mycol.update_one(myquery, newvalues)

# 输出修改后的  "sites"  集合
for x in mycol.find():
    print(x)
