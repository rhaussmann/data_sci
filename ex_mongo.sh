#!/usr/bin/env bash

# start Services
brew services start mongodb

# open mongo terminal
mongo

# see databases
show dbs

# Switch to database
use mydb

# Insert into collection
db.users.insert({name: 'Jon', age: '45', friends: ['Henry', 'Ashley']})

# List Collections
 db.getCollectionNames()

# Get data
 db.usersfind()
 db.users.findOne()

# Query
# find by a single value of a field
db.users.find({name: 'Jon'})

# find if a field exists
db.users.find({car: {$exists: true}})

# Find by value in an array
db.users.find({friends: 'Henry'})

# Return only some fields
db.users.find({}, {name: true}):

#Update
db.users.update({name: "Jon"}, {$set: {friends: ["Phil"]}})
db.users.update({name: "Jon"}, {$push: {friends: "Susie"}})






