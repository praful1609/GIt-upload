import pymongo
client = pymongo.MongoClient("mongodb+srv://praful:praful1609@cluster0.h9nnl.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= {"name" : "praful",
      "email_id" : "prafulbhojane1609@gmail.com",
      "surname" : "bhojane"}


db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )