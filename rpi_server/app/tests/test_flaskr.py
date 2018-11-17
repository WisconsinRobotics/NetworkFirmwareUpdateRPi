import os
import tempfile
import sys
import pytest
from flask import flash, Flask, request, redirect, render_template, \
							 url_for, send_from_directory
sys.path.append('../../')
sys.path.append('../')
from app import app
import routes




@pytest.fixture
def client():
# Setup for relative file paths
	app = Flask(__name__, instance_relative_config=True)
	app.config['TESTING'] = True
	client = app.test_client(follow_redirects=False)
	yield client



"""

def test_example():

	with app.app_context():
		with app.test_request_context('/upload', method = 'GET'):
			routes.upload()
"""
