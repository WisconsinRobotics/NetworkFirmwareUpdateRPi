# Home page URLs and their functions
import os
from app 			import app
from flask 			import flash, Flask, request, redirect, render_template, \
				  		   url_for, send_from_directory
from werkzeug.utils import secure_filename
									# Where to save uploaded images
UPLOAD_FOLDER = '/media/tim/HDD/workspace/server/app/firmwareImages'
ALLOWED_EXTENSIONS = set(['bin'])	# Only .bin image files allowed

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):			# Enforce allowed filename extensions
	return '.' in filename and \
		filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def root():
	return 'Root directory'

@app.route('/index')
def index():
	return 'Index'

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
	if request.method == 'POST':	# Respond to POST requests
		
		if 'file' not in request.files:	# Check if request contains file
			print 'No file part'
			return redirect(request.url)
		file = request.files['file']
		
		if file.filename == '':			# Check if user selected a file
			print 'No selected file'
			return redirect(request.url)
										# Check if allowed, sanitize input
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return redirect(request.url)
			
	return render_template('upload.html')
		
@app.route('/upload/<filename>')
def image_file(filename):			# Return uploaded image
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
	
with app.test_request_context():
	print(url_for('index'))
	print(url_for('upload'))
	print(url_for('upload', next = '/'))
