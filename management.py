import os
import pymongo

class management:
    connection_string: str

    def __init__(self) -> None: 
        self.connection_string = os.getenv('JUKE')
        self.col = pymongo.MongoClient(self.connection_string)['jukebox']['songs']


    class song(object):
        
        name:str
        filename:str
        interpret:str
        album:str
        genre:str
        releasedate: any
        data: bytes

        def __init__(self, input_name, input_filename, input_interpret = "", input_album = "", input_genre = "", input_releasedate = None, input_data=None) -> None:
            self.name = input_name
            self.filename = input_filename
            self.interpret = input_interpret
            self.album = input_album
            self.genre = input_genre
            self.releasedate = input_releasedate
            if input_data == None:
                try:
                    with open(f'export_songs/{self.filename}', 'rb') as song_file:
                        self.data =  bytes(song_file.read())
                except Exception as e:
                    print(str(e))
            else:
                self.data = input_data

    def get_song(filter = "") -> song:
        document = management.col.find(filter)[0]
        song = management.song(document['name'], document['filename'], document['interpret'], document['album'], document['genre'], document['releasedate'], document['data'])
        with open(f'import_songs/{song.filename}', 'wb') as song_file:
            song_file.write(song.data)
        return song


    def insert_song(song: song):
        management.col.insert_one(song.__dict__)

