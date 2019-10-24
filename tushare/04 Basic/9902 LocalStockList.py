# 查询指定字段的数据
# 我们可以使用 find() 方法来查询指定字段的数据，将要返回的字段对应值设置为 1。

import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myclient = pymongo.MongoClient('mongodb://chenqingwh.uicp.net:37017/')
mydb = myclient["quant_01"]
mycol = mydb["gps"]
mycol2 = mydb["stocks"]
# recordcount = 0

# pymongo.cursor.Cursor
cur = mycol.find({}, {"_id": 0, "id": 1, "name": 1})

array = list(cur)
print(type(array))
print(len(array))


# # 获取列表的第二个元素
# def takeSecond(elem):
#     return elem[1]
#
#
# array.sort(key=takeSecond, reverse=False)
stockList = []
stockSet1 = set()
for x in array:
    # print(x)
    stockList.append(x['id'])
    stockSet1.add(x['id'])

stockList.sort()
# print(stockList)

print('-------------------------------------')

cur2 = mycol2.find({}, {"_id": 0, "code": 1})
# for x in cur2:
#     print(x)

array2 = list(cur2)  # posts是我的collection
# print(type(array))
# print(len(array))
# array.sort(key=takeSecond, reverse=False)
stockList2 = []
stockSet2 = set()
for x2 in array2:
    # print(x2)
    stockList2.append(x2['code'])
    stockSet2.add(x2['code'])

stockList2.sort()
# print(stockList2)

stockSetDiff = stockSet1.difference(stockSet2)
print(stockSetDiff)


# for x in mycol.find({}, {"_id": 0, "name": 1, "alexa": 1}):
#     print(x)

# 除了 _id 你不能在一个对象中同时指定 0 和 1，如果你设置了一个字段为 0，则其他都为 1，反之亦然。

print('-------------------------------------')
# 以下实例除了 alexa 字段外，其他都返回：

# for x in mycol.find({}, {"alexa": 0}):
#     print(x)
