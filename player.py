from management import management
from pymongo import MongoClient

client = MongoClient("mongodb+srv://jukebox:jukebox@cluster0.hehg9fc.mongodb.net/")
db = client["jukebox"]
songs_collection = db["songs"]

def selectDocument():
    docs = songs_collection.find({})
    docs_count = songs_collection.count_documents({})
    for i in range(docs_count):
        print(f'{i} ): song_id: {(docs[i]["_id"])}')
    try:
        doc_select = int(input(f'select Document (0-{docs_count-1}): '))
        if doc_select in list(range(0, len(docs_count)-1)):
            id = docs[doc_select]["_id"]
            return id
        else:
             print('Input not in range')
    except Exception as e:
        print(str(e))

def selectOperation(id):
    operations = ['play', 'edit', 'delete', 'add to playlist']
    for i in range(len(operations)):
          print(f'{i} ): {operations[i]}')
    op_select = int(input(f'select Operation (0-{len(operations)-1}): '))
    if op_select in list(range(0, len(operations)-1)):
         
        # Edit
        if op_select == operations.index('edit'):
             query = input('Data to change as query: ')
             management.edit_song(query)

        # Edit
        if op_select == operations.index('delete'):
             management.delete_song()

    else:
         print('Input not in range')
         

def main():
    id = selectDocument()
    selectOperation(id)


if __name__ == "__main__":
        main()