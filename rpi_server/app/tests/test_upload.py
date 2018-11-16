import os
import tempfile
import sys
import pytest
import unittest
from flask import flash, Flask, request, redirect, render_template, \
							 url_for, send_from_directory
from flask_testing import TestCase


sys.path.append('../../')
sys.path.append('../')
from app import app
import routes




def test_upload_No_File_Selected(client, app):
	with app.app_context():
		response = client.post('/upload')
		print(response.data)
		assert("No file selected" in response.data)

def test_upload_Invalid_File_Type(client, app):
	with app.app_context():
		with open('../../../fake_firmware.bin', 'rb') as f:
    			#r = requests.post('http://httpbin.org/post', files={'report.xls': f})
			data = dict( file=(f, "work_order.123"),)
			response = client.post('/upload', content_type='multipart/form-data',data=data)
			print(response.data)
			assert("Invalid file type. Requires .bin file type. Filename =" in response.data)

def test_upload_Success(client, app):
	with app.app_context():
		with open('../../../fake_firmware.bin', 'rb') as f:
    			#r = requests.post('http://httpbin.org/post', files={'report.xls': f})
			data = dict( file=(f, f.name),)
			response = client.post('/upload', content_type='multipart/form-data',data=data)
			print(response.data)
			assert("Successful upload" in response.data)

