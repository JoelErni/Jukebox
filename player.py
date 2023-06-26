import re
import json
from management import management
from pymongo import MongoClient

client = MongoClient("mongodb+srv://jukebox:jukebox@cluster0.hehg9fc.mongodb.net/")
db = client["jukebox"]
songs_collection = db["songs"]

def selectDocument():
    search = input('search: ')

    filter = {'$or': [{"name": re.compile(f'.*{search}.*', re.IGNORECASE)},{"interpret": re.compile(f'.*{search}.*', re.IGNORECASE)}, { "album": re.compile(f'.*{search}.*', re.IGNORECASE)}, {"genre": re.compile(f'.*{search}.*', re.IGNORECASE)}, {"releasedate": re.compile(f'.*{search}.*', re.IGNORECASE)}]}
    docs = songs_collection.find(filter)
    docs_count = songs_collection.count_documents(filter)
    if docs_count > 0:
        for i in range(0,docs_count):
            print(f'{i} ): song: {docs[i]["interpret"]} - {docs[i]["name"]}')
        try:
            doc_select = int(input(f'select Document (0-{docs_count-1}): '))
            if doc_select in list(range(0, docs_count)):
                id = docs[doc_select]["_id"]
                selectOperation(id)
            else:
                print('Input not in range')
        except Exception as e:
            print(str(e))
    else:
         print("no songs found :c")

def selectOperation(id):
    operations = ['play', 'edit', 'delete', 'add to playlist', 'details']
    for i in range(len(operations)):
          print(f'{i} ): {operations[i]}')
    op_select = int(input(f'select Operation (0-{len(operations)-1}): '))
    if op_select in list(range(0, len(operations))):
         
        # Play
        if op_select == operations.index('play'):
             management.play_song(id)
        
        # Edit
        if op_select == operations.index('edit'):
             query = json.loads(input('Data to update as query: '))
             management.edit_song(id, query)

        # Edit
        if op_select == operations.index('delete'):
             management.delete_song(id)

        # Add to playlist


        #Get Songinfo
        if op_select == operations.index('details'):
             management.get_song_info(id)
    else:
         print('Input not in range')
         
def addSong():
     songname = input('Songname: ')
     filename = input('Filename: ')
     interpret = input('Interpret: ')
     album = input('Album: ')
     genre = input('Genre: ')
     releasedate = input('Releasedate: ')
     song = management.song(songname, filename, interpret, album, genre, releasedate)
     management.insert_song(song)

def main():
    selectMenu = input('0 ): Add song\n1 ): Search song\n')
    if selectMenu == '0':
        addSong()
    elif selectMenu == '1':
        selectDocument()


if __name__ == "__main__":
        main()