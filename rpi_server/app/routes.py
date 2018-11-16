
## Home page URLs and their functions

# System imports
import datetime
import os
import socket
import requests 

# Server imports
from app import app, UPLOAD_FOLDER
from flask import Flask, request, redirect, render_template, \
                             url_for, send_from_directory, jsonify

from werkzeug.utils import secure_filename

# DB imports
import sqlite3 as sql
from app import db

# Only .bin image files allowed
ALLOWED_EXTENSIONS = set(['bin'])
UPLOAD_FOLDER = app.root_path + '/firmwareImages'

app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):            # Enforce allowed filename extensions
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/upload', methods=['GET', 'POST'])
def upload():
    # Respond to POST requests
    if request.method == 'POST':
        
        # Check if request contains file
        if 'file' not in request.files:
            print('No file part')
            return redirect(url_for('index'))
        file = request.files['file']

        # Check if user selected an allowed file
        if file.filename == '' or not allowed_file(file.filename):
            print('File not selected or file extension not allowed')
            return redirect(url_for('index'))

        # Store the file
        if file:
            # Sanitize filename (useless now)
            filename = secure_filename(file.filename)

            # Use timestamp as filename
            filename = str(datetime.datetime.now())

            # Check if upload path exists, make it
            if not os.path.exists(UPLOAD_FOLDER):
                os.makedirs(UPLOAD_FOLDER)

            # Save file named by timestamp
            file.save(UPLOAD_FOLDER + '/' + filename)

            # Add to DB
            db.add_img(filename)

        # Close uploaded file
        file.close()

    return redirect(url_for('index'))

# Uploads a file to user/robot
@app.route('/api/download/<filename>')
def image_file(filename):
    # Upload saved image to requester
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# List all uploaded images, ordered recent first


@app.route('/api/history', methods=['GET'])
def history():
    # Get populated HTML page
    page = db.list_imgs()
    rows = page[1]
    page = page[0]

    # Return populated page
    return render_template(page,rows = rows)

@app.route('/api/selectHistory', methods=['POST'])
def select_history():
    # Get populated HTML page
    page = db.list_imgs()
    rows = page[1]
    page = page[0]
    
    # Return populated page
    return render_template(page,rows = rows)

def uploadMicroprocessor(filepath):
    HOST = '127.0.0.1'  # IP address of the microprocessor
    PORT = 12579        # Port to listen on
    with socket.socket() as s:
        s.connect((HOST, PORT))

        # send file size first
        file_size = os.path.getsize(filepath).to_bytes(2, byteorder='big')
        s.sendall(file_size)

        # Check clear to send
        cts = s.recv(4)
        cts = int.from_bytes(cts, byteorder='big')

        # Send file if clear to send received
        if cts == 1:
            with open(filepath, 'rb') as f:
                image = f.read()
                s.sendall(image)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")

@app.route('/index')
def index():
    if app.debug:
        return requests.get('http://localhost:8080/').text
    return render_template("index.html")
