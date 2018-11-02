# Home page URLs and their functions
import os
import socket
from app import app
from flask import flash, Flask, request, redirect, render_template, \
                             url_for, send_from_directory
from werkzeug.utils import secure_filename

# Where to save uploaded images
UPLOAD_FOLDER = app.root_path + '/firmwareImages'
ALLOWED_EXTENSIONS = set(['bin'])    # Only .bin image files allowed

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
    return render_template('index.html')

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':    # Respond to POST requests

        if 'file' not in request.files:    # Check if request contains file
            print('No file part')
            return redirect(url_for('index'))
        file = request.files['file']

        if file.filename == '' or not allowed_file(file.filename):            # Check if user selected a file
            print('File not selected or file extension not allowed')
            return redirect(url_for('index'))

        # Check if allowed, sanitize input
        if file:
            filename = secure_filename(file.filename)
            if not os.path.exists(UPLOAD_FOLDER):
                os.makedirs(UPLOAD_FOLDER)
            filepath = UPLOAD_FOLDER + '/' + filename
            file.save(filepath)
            uploadMicroprocessor(filepath)
            return redirect(url_for('index'))

@app.route('/upload/<filename>')
def image_file(filename):            # Return uploaded image
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

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
