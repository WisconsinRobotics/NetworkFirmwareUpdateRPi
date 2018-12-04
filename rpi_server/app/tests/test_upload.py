import os
import tempfile
import sys
import pytest
import unittest
from flask import flash, Flask, request, redirect, render_template, \
							 url_for, send_from_directory



sys.path.append('../../')
sys.path.append('../')
from app import app
import routes




def test_upload_No_File_Selected(client, app, capsys):
	with app.app_context():
		response = client.post('/api/upload')
		print(response.data)
		out, err = capsys.readouterr()
		assert("No file part" in out)

def test_upload_Invalid_File_Type(client, app, capsys):
	with app.app_context():
		with open('./dummy.bin', 'rb') as f:
    			#r = requests.post('http://httpbin.org/post', files={'report.xls': f})
			data = dict( file=(f, "work_order.123"),)
			response = client.post('/api/upload', content_type='multipart/form-data',data=data)
			print(response.data)
			out, err = capsys.readouterr()
			assert("File not selected or file extension not allowed" in out)
			#assert(b"Invalid file type. Requires .bin file type. Filename =" in response.data)

def test_upload_Success(client, app, capsys):
	with app.app_context():
		with open('./dummy.bin', 'rb') as f:
    			#r = requests.post('http://httpbin.org/post', files={'report.xls': f})
			data = dict( file=(f, f.name),)
			response = client.post('/api/upload', content_type='multipart/form-data',data=data)
			print(response.data)
			out, err = capsys.readouterr()
			assert("File not selected or file extension not allowed" in out)
			#assert(b"Successful upload" in response.data)

def test_upload_Failure(client, app, capsys):
	with app.app_context():
		with open('./dummy.bin', 'rb') as f:
    			#r = requests.post('http://httpbin.org/post', files={'report.xls': f})
			data = dict( file=(f, f.name),)
			response = client.post('/api/upload', content_type='multipart/form-data',data=data)
			print(response.data)
			out, err = capsys.readouterr()
			assert('Failed to connect to Microcontroller' in out)
			#assert(b"Successful upload" in response.data)

def test_uploadMicroprocessor():
	success_message = routes.uploadMicroprocessor('../../../fake_firmware.bin')
	assert("file sent successfully" in success_message) 
	

