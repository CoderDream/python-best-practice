# 返回指定条数记录
# 如果我们要对查询结果设置指定条数的记录可以使用 limit() 方法，该方法只接受一个数字参数。

# 以下实例返回 3 条文档记录：

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]

myresult = mycol.find().limit(3)

# 输出结果
for x in myresult:
    print(x)
