from pymongo import MongoClient

client = MongoClient("mongodb+srv://jukebox:jukebox@cluster0.hehg9fc.mongodb.net/")
db = client["jukebox"]
songs_collection = db["songs"]
