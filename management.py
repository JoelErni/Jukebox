import bson
import os
import pymongo
connection_string = 'mongodb+srv://jukebox:jukebox@cluster0.hehg9fc.mongodb.net/'
col = pymongo.MongoClient(connection_string)['jukebox']['songs']

class management:
    class song(object):
        def __init__(self, input_name, input_filename, input_interpret = "", input_album = "", input_genre = "", input_releasedate = None, input_data=None) -> None:
            self.name = input_name
            self.filename = input_filename
            self.interpret = input_interpret
            self.album = input_album
            self.genre = input_genre
            self.releasedate = input_releasedate
            if input_data == None:
                try:
                    if not os.path.exists('/export_songs'):
                        os.mkdir('/export_songs')
                    with open(f'export_songs/{self.filename}', 'rb') as song_file:
                        self.data =  bytes(song_file.read())
                except Exception as e:
                    print(str(e))
            else:
                self.data = input_data

    def downlaod_song(filter = "") -> song:
        document = col.find(filter)[0]
        song = management.song(document['name'], document['filename'], document['interpret'], document['album'], document['genre'], document['releasedate'], document['data'])
        if not os.path.exists('/import_songs'):
            os.mkdir('/import_songs')
        with open(f'import_songs/{song.filename}', 'wb') as song_file:
            song_file.write(song.data)
        return song

    def find_songs(filter)->list:
        docs = col.find(filter)
        return docs

    def insert_song(song: song):
        col.insert_one(song.__dict__)

    def delete_song():
        docs = col.find({}, {'data': 0})
        count = col.count_documents({})
        for i in range(count):
            id = docs[i]['_id']
            print(f'{i}) id: {id}')
        try:
            selected_doc = int(input(f'Select document (0-{count-1}): '))
        except Exception as e:
            print(str(e))
        if selected_doc in list(range(0, count)):
            col.delete_one({'_id': bson.ObjectId(docs[selected_doc]['_id'])})
        else:
            print("no document found")

    def edit_song(update):
        docs = col.find({}, {'data': 0})
        count = col.count_documents({})
        for i in range(count):
            id = docs[i]['_id']
            print(f'{i}) id: {id}')
        try:
            selected_doc = int(input(f'Select document (0-{count-1}): '))
        except Exception as e:
            print(str(e))
        if selected_doc in list(range(0, count)):
            col.update_one({'_id': bson.ObjectId(docs[selected_doc]['_id'])}, {'$set': update})
        else:
            print("no document found")

management.delete_song()