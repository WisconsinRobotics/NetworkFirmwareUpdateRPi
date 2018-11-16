## SQLite3 DataBase

# System imports
import os

# DB imports
import sqlite3 as sql
from flask import g

#Server imports
from app   import app
from app   import routes

# Location of DB
DATABASE = app.root_path + '/firmwareImages/database.db'

# Establishes DB connection, reused in subsequent calls
def get_db():
    # Create DB file if needed
    open(DATABASE, 'a').close()

    # Get DB handle
    db = getattr(g, app.config['DATABASE'], None)
    
    # Create DB connection if needed
    if db is None:
        db = g.db = sql.connect(app.config['DATABASE'])
        
    # Create DB connection if needed
    #if 'db' not in g:
    #            
    #    g.db = sql.connect
    #    (
    #        app.config['DATABASE']
    #        #detect_types = sql.PARSE_DECLTYPES
    #    )
    #    g.db.row_factory = sql.Row

    # Return DB ptr
    return db

# Deinitialize the DB
def close_db(e=None):
    # Close DB connection
    db = g.pop('db', None)

    if db is not None:
        db.close()

# Initialize the DB
def init_db():

    # Setup DB location
    app.config['DATABASE'] = DATABASE

    db = get_db()

    # Use the schema
    with app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

# Add a new image to DB
def add_img(name):
    # Connect to the DB
    con = get_db()
    cur = con.cursor()
    
    try:
        # Insert a new entry
        con.execute('''INSERT INTO images (name)
                       VALUES (?)''', (name,))

        # Write changes to DB
        con.commit()
        print('Added a new image to DB')
        
    except:
        # Revert changes upon failure
        con.rollback()
        print('Failed to add image to DB')

# Start the DB immediately
with app.app_context():
    init_db()
