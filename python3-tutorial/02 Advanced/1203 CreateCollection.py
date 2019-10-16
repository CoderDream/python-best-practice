#!/usr/bin/python3

import pymongo

myclient = pymongo.MongoClient('mongodb://chenqingwh.uicp.net:37017/')
mydb = myclient["quant_01"]

mycol = mydb["sites"]
