## Home page URLs and their functions

# System imports
import datetime
import json
import os
import socket
import requests
import subprocess

# Server imports
from app import app
from app import UPLOAD_FOLDER
from app import GH_URL, GH_UN, GH_PASS

from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import url_for
from flask import send_from_directory

# DB imports
import sqlite3 as sql
from app import db

# Set timestamp format
datetime.timedelta(1000000)

# Only .bin image files allowed
ALLOWED_EXTENSIONS = set(['bin'])

# Setup for relative file paths
app = Flask(__name__, instance_relative_config=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):            # Enforce allowed filename extensions
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def root():
    return redirect(url_for('index'))

# Shows the home page
@app.route('/index')
def index():
    # Get image history list
    rows = db.list_imgs()

    # Get GitHub image list
    #response = github()

    #print(str(response.json())[0:64])

    # Return populated page
    return render_template('index.html', rows = rows)

# Downloads a file to server
@app.route('/upload', methods = ['GET', 'POST'])
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
            # Use timestamp as filename
            filename = str(datetime.datetime.now())
            filename = filename.replace(" ","") + '.bin'

            # Check if upload path exists, make it
            if not os.path.exists(UPLOAD_FOLDER):
                os.makedirs(UPLOAD_FOLDER)

            # Save file named by timestamp
            file.save(UPLOAD_FOLDER + '/' + filename)

            # Add to DB
            db.add_img(filename)

            try:
                # Send file to microcontroller
                uploadMicroprocessor(UPLOAD_FOLDER + '/' + filename)
            except:
                print('Failed to connect to Microcontroller')

        # Close uploaded file
        file.close()

    return redirect(url_for('index'))

# Uploads a file to user/robot
@app.route('/download/<filename>')
def image_file(filename):
    # Upload saved image to requester
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Get GitHub images list
def github():
    # Authenticate to GitHub TODO use secure key
    os.system('curl -i https://api.github.com -u ' + GH_UN + ':' + GH_PASS)

    # GET JSON from GitHub
    response = requests.get(GH_URL)

    return response

# Send an image to the microcontroller
def uploadMicroprocessor(filepath):
    HOST = '127.0.0.1'  # IP address of the microprocessor
    PORT = 12579        # Port to listen on
    with socket.socket() as s:
        s.connect((HOST, PORT))

        # send file size first
        file_size = os.path.getsize(filepath)
        s.sendall(file_size.to_bytes(4, byteorder='little'))

        # Check clear to send
        cts = s.recv(4)
        cts = int.from_bytes(cts, byteorder='little')
        print(cts)

        # Send file if clear to send received
        if cts == file_size:
            with open(filepath, 'rb') as f:
                image = f.read()
                s.sendall(image)
                rcv = s.recv(4)
                rcv = int.from_bytes(rcv, byteorder='little')
                print(rcv)
