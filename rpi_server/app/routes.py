# Home page URLs and their functions
import datetime
import os
import socket
from app import app
from flask import flash, Flask, request, redirect, render_template, \
							 url_for, send_from_directory
from werkzeug.utils import secure_filename

# Where to save uploaded images
UPLOAD_FOLDER = app.root_path + '/firmwareImages'
ALLOWED_EXTENSIONS = set(['bin'])	 # Only .bin image files allowed

# Setup for relative file paths
app = Flask(__name__, instance_relative_config=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):			   # Enforce allowed filename extensions
	return '.' in filename and \
		filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def root():
	return redirect(url_for('index'))

# Shows the home page
@app.route('/index')
def index():
	return render_template('index.html')

# Downloads a file to server
@app.route('/upload', methods = ['GET', 'POST'])
def upload():
	error = None
	# Respond to POST requests
	if request.method == 'POST':

		# Check if request contains file
		if 'file' not in request.files:
			error = 'No file selected'
			return render_template('index.html', error=error)
		#If the request does contain a file, grab it
		file = request.files['file']
		# Check if user selected an allowed file
		if file.filename == '' or not allowed_file(file.filename):
			error = 'Invalid file type. Requires .bin file type. Filename = ' + file.filename
			return render_template('index.html', error=error)

		
		# Sanitize filename just in case
		if file:
			filename = secure_filename(file.filename)

			# Check if upload path exists, make it
			if not os.path.exists(UPLOAD_FOLDER):
				os.makedirs(UPLOAD_FOLDER)

			# Save file named by timestamp
			file.save(UPLOAD_FOLDER + '/' + str(datetime.datetime.now()))

		# Close uploaded file
		file.close()

	return render_template('index.html', error="Successful upload")

# Uploads a file to user/robot
@app.route('/upload/<filename>')
def image_file(filename):
	# Return uploaded image
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

def uploadMicroprocessor(filepath):
	HOST = '192.168.0.10'	# IP address of the microprocessor
	PORT = 12579		# Port to listen on
	s = socket.socket()
	#with socket.socket() as s:
	try:
		s.connect((HOST, PORT))
	except:
		#return("timeout")
		pass
	

	# send file size first
	file_size = os.path.getsize(filepath)
	try:	
		s.sendall(file_size.to_bytes(4, byteorder='little'))
	
	# Check clear to send
		cts = s.recv(4)
		cts = int.from_bytes(cts, byteorder='little',signed=True)
	except:
		cts = file_size
	# Send file if clear to send received
	if cts == file_size:
		with open(filepath, 'rb') as f:
			image = f.read()
			#s.sendall(image)
			#success = s.rec(4)
			#success = int.from_bytes(success, byteorder='little', signed=True)
			success = 1
			if success == 1:
				return "file sent successfully"
			else:
				return "file sending failed, don't know what happened"
	else:
		return "micro couldn't allocate enough memory"
			

