# Requires pymongo 3.6.0+
from pymongo import MongoClient

client = MongoClient("mongodb://chenqingwh.uicp.net:37017/")
database = client["quant_01"]
collection = database["gps"]

# Created with Studio 3T, the IDE for MongoDB - https://studio3t.com/

# query = {"local":"sh"}

# query = {"id": "000016"}
# 国债回购（席位托管方式）
# query = {"id": {"$regex": "^201"}, "local": "sh"}

# query = {"id": {"$regex": "^600"}, "local": "sh"}
# query = {"id": {"$regex": "^60[0-1]"}, "local": "sh"}


# query = {"id": {"$regex": "^70[0-1]"}, "local": "sh"}


# query = {"id": {"$regex": "^03"}, "local": "sz"}


query = {"id": {"$regex": "^78"}, "local": "sh"}

# cursor = collection.find(query, skip=4948, limit=50)
cursor = collection.find(query)
try:
    for doc in cursor:
        print(doc)
finally:
    client.close()
