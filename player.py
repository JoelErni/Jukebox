from pymongo import MongoClient

client = MongoClient("mongodb+srv://jukebox:jukebox@cluster0.hehg9fc.mongodb.net/")
db = client["jukebox"]
songs_collection = db["songs"]

def search_songs(search_params):
    search_params = {k: v.lower() for k, v in search_params.items()}

    query = {}
    if "name" in search_params:
        query["name"] = {"$regex": search_params["name"]}
    if "interpret" in search_params:
        query["interpret"] = {"$regex": search_params["interpret"]}
    if "album" in search_params:
        query["album"] = {"$regex": search_params["album"]}
    if "genre" in search_params:
        query["genre"] = {"$regex": search_params["genre"]}

    result = songs_collection.find(query)

    return list(result)

search_params = {
    "name": "",
    "interpret": "",
    "album": "",
    "genre": ""
}
results = search_songs(search_params)
for song in results:
    print(song)
