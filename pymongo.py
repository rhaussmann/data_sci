from pymongo import MongoClient
mongo_client = MongoClient()
db = mongo_client.mydb2
coll = db.users

coll.insert({'name': 'Jon', 'age': '45', 'friends': ['Henry', 'Ashley']})
coll.insert({'name': 'Ashley', 'age': '37', 'friends': ['Jon', 'Henry']})
coll.insert({'name': 'Frank', 'age': '17', 'friends': ['Billy'], 'car': 'Civic'})

print "All entries:"
print list(coll.find())
print

print "Just one:"
print coll.find_one()
print

print "Just Ashley:"
print coll.find_one({'name': 'Ashley'})
print

print "Added Jon's car"
coll.update({'name': "Jon"}, {'$set': {'car': "Prius"}})
print coll.find_one({'name': 'Jon'})
print

print "Added Jon's new friend Billy"
coll.update({'name': "Jon"}, {'$push': {'friends': "Billy"}})
print coll.find_one({'name': 'Jon'})

