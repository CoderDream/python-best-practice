import pymongo

myclient = pymongo.MongoClient('mongodb://chenqingwh.uicp.net:37017/')
mydb = myclient["quant_01"]
mycol = mydb["sites"]

mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}

x = mycol.insert_one(mydict)
print(x)
print(x)
