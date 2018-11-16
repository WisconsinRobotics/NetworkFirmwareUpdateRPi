## Start up server and DB, imports must come after global declarations!

# Initialize package called app
from flask import Flask

app = Flask(__name__)

import os

# Initialize where to save images
UPLOAD_FOLDER = app.root_path + '/firmwareImages'

# Check if upload path exists, make it
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Location of DB
DATABASE = UPLOAD_FOLDER + '/database.db'

from app import routes, db

# Initialize DB
with app.app_context():
    db.init_db()
