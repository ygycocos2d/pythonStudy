# -*- coding: utf-8 -*-
import pymongo
conn = pymongo.MongoClient('127.0.0.1',27017)
db = conn.test

print db.collection_names()

db.user.insert({'name':'hj'})

print db.user.find()

db.user.insert({"name":1})

print db.user.find().count()

##
db2 = conn.test2

print db2.collection_names()

db2.user.insert({"三国杀":1})

print db2.collection_names()

for item in db.user.find():
    print item



