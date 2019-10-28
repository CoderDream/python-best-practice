import pymongo


# client = MongoClient("mongodb://chenqingwh.uicp.net:37017/")
# db = client["quant_01"]

# 起始数据：
# db.Blog.insert_one({"_id": "123456", "blog_cont": "abcdef", "title": "《My Test》"})
# db.Blog.find()


class UpdateDemo:
    def __init__(self):
        self.DB_CONN = pymongo.MongoClient('mongodb://chenqingwh.uicp.net:37017')['quant_01']
        self.db = self.DB_CONN["Blog"]

    def insert_one(self):
        self.db.insert_one({"_id": "123456", "blog_cont": "abcdef", "title": "《My Test》"})

    def update_one(self):
        # self.db.update_one({"_id": "123456"}, {'$setOnInsert': {"blog_cont": "abc123", "other": "hello world!"}})
        self.db.update_one({"_id": "123456"}, {'$set': {"blog_cont": "abc124", "other": "hello world!"},
                                               '$setOnInsert': {'defaultQty': 100}}, upsert=True)

    # def update_one_insert(self):
    #     self.db.update_one({"id": "123456"}, {'$setOnInsert': {"blog_cont": "abc123", "other": "hello world!"}, { '$upsert': true }})

    def find(self):
        return list(self.db.find())


if __name__ == '__main__':
    update_demo = UpdateDemo()
    # update_demo.insert_one()
    update_demo.update_one()
    # update_demo.update_one_insert()
    print(update_demo.find())
