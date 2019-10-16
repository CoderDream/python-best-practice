# 使用正则表达式查询
# 我们还可以使用正则表达式作为修饰符。

# 正则表达式修饰符只用于搜索字符串的字段。

# 以下实例用于读取 name 字段中第一个字母为 "R" 的数据，正则表达式修饰符条件为 {"$regex": "^R"} :

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["site3"]

myquery = {"name": {"$regex": "^R"}}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)
