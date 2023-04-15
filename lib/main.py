from peewee import *
import datetime

# Database connection
db = PostgresqlDatabase(
    'notes', 
    user='', 
    password='',
    host='localhost', 
    port=5432)

db.connect()

# Define models
class BaseModel(Model):
    class Meta:
        database = db

class Note(BaseModel):
    title = CharField()
    body = TextField()
    # tags = Lis # Find out way of adding a list of identifying tags
    date_added = DateTimeField(default=datetime.datetime.now)

# Drop table if exists
db.drop_tables([Note])

# Create table
db.create_tables([Note])

new_note = Note(title='Test', body='Testing of db connection')
new_note.save()

# List all notes
list_all = Note.select()
print([[note.title, note.body] for note in list_all])