# Requires pymongo 3.6.0+
from pymongo import MongoClient

client = MongoClient("mongodb://chenqingwh.uicp.net:37017/")
database = client["quant_01"]
collection = database["gps"]

# Created with Studio 3T, the IDE for MongoDB - https://studio3t.com/

query = {}

cursor = collection.distinct("local")
try:
    for doc in cursor:
        print(doc)
finally:
    client.close()
