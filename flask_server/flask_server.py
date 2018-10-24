from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def hello(name=None):
	return render_template('vue_boot_example.html', name=name)
    #return 'Hello, World!'