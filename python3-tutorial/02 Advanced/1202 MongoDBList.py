import pymongo

myclient = pymongo.MongoClient('mongodb://chenqingwh.uicp.net:37017/')

dblist = myclient.list_database_names()
# dblist = myclient.database_names()
for dbname in dblist:
    print(dbname)
