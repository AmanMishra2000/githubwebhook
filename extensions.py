from flask_pymongo import PyMongo

import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["githubevents"]
collection = db["githubactions"]
