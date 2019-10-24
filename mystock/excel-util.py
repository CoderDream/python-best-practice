import pandas as pd
import sys
import pymongo

local = 'sz'

# , sheetname='sz'
file_path = sys.path[0] + '\data\codetype.xlsx'
df = pd.read_excel(file_path, sheet_name=local)

# print(sys.path[0])
# print(df)
#
# prefix  type            comments

# data = df.iloc[1, 1]  # 读取第一行第二列的值，这里不需要嵌套列表
# print("读取指定行的数据：{0}".format(data))
# data_value = int(format(data))
# if data_value < 10:
#     prefix = '00' + str(data_value)
# if data_value < 100 and data_value >= 10:
#     prefix = '0' + str(data_value)
#
# print("读取指定行的数据：{0}".format(prefix))

test_data = []
for i in df.index.values:  # 获取行号的索引，并对其进行遍历：
    # 根据i来获取每一行指定的数据 并利用to_dict转成字典
    # row_data = df.loc[i, ['prefix', 'type', 'comments']].to_dict()
    data_temp = df.iloc[i, 0]
    # print("读取指定行的数据：{0}".format(data_temp))

    data_value = int(format(data_temp))
    if data_value < 10:
        prefix = '00' + str(data_value)
    if data_value < 100 and data_value >= 10:
        prefix = '0' + str(data_value)

    print("读取指定行的数据：{0}".format(prefix))

    data_temp1 = int(df.iloc[i, 1])
    data_temp2 = df.iloc[i, 2]

    row_data = {'local': local, 'prefix': prefix, 'type': data_temp1, 'comments': data_temp2}  # df.loc[i, ['type', 'comments']].to_dict()
    test_data.append(row_data)
print("最终获取到的数据是：{0}".format(test_data))

myclient = pymongo.MongoClient('mongodb://chenqingwh.uicp.net:37017/')
mydb = myclient["quant_01"]
mycol = mydb["codetype"]

# mylist = [
#     {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
#     {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
#     {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
#     {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
#     {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
# ]
# buffer=[]
# for item in mylist:
#     buffer.append(InsertOne(item))
# mycol.bulk_write(buffer, ordered=False)
x = mycol.insert_many(test_data)

# bson.errors.InvalidDocument: cannot encode object: 1, of type: <class 'numpy.int64'