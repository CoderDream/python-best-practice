# 查询一条数据
# 我们可以使用 find_one() 方法来查询集合中的一条数据。

# 查询 sites 文档中的第一条数据：


import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]

x = mycol.find_one()

print(x)
