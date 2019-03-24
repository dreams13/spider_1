from pymongo import MongoClient

client = MongoClient()
dbs = client['admin']
dbs.authenticate('python','python')
col = client['test']['stu']
rets = col.find({})
print(rets)
for ret in rets:
    print(ret)