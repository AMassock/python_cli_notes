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
def remove_all():
    db.drop_tables([Note])

# Create table
db.create_tables([Note])

# 
def repeat():
    reload = input("Would you like to continue? Y/N \n").lower()
    if reload == 'y':
        options()
    else:
        exit()

# List all notes
def list_all():
    list_all = Note.select()
    for note in list_all:
        title = note.title
        body = note.body
        print(f"Title: {title}")
        print(f"Body: {body}")

# List one note based off title
def get_single_note():
    search_title = input('What is the title of the note youre looking for? \n')
    get_one = Note.get(title=search_title)
    print(get_one.body)

# Create new note
def create_new():
    title = input('What is the title? \n')
    body = input('What is your note? \n')
    new_note = Note(title=title, body=body)
    new_note.save()

# Remove note based off title

# Update note based off title

# Create conditional to prompt user for options
def options():
    print("Welcome to your terminal note taking app.\n Please choose from the following options: \n 1: List all notes \n 2: Find Note based off Title \n 3: Create new Note \n 4: Delete ALL Notes")
    selection = input('Please insert selection: ')
    if selection == '1':
        list_all()
        repeat()
    elif selection == '2':
        get_single_note()
        repeat()
    elif selection == '3':
        create_new()
        print('New note created.')
        repeat()
    elif selection == '4':
        remove_all()
        print('All notes deleted!')
        repeat()
    else:
        print('Sorry that is an incorrect selction. Please type the number representing the thing you would like to do')
        options()

options()