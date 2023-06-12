import os
os.environ['JUKE'] = "mongodb+srv://jukebox:jukebox@cluster0.hehg9fc.mongodb.net/"
print(os.getenv('JUKE'))