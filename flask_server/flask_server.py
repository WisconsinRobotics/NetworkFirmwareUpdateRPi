import os
from flask import Flask, request
from flask import render_template

UPLOAD_FOLDER = '/test'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/home')
def hello(name=None):
	return render_template('vue_boot_example.html', name=name)
    #return 'Hello, World!'
@app.route('/file_upload', methods=['GET', 'POST'])
def file_upload(name=None):
	file = request.files['datafile']
	filename = file.filename
	file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	print("File upload!")
	return render_template('flask_html_test.html', name=name)
    #return 'Hello, World!'