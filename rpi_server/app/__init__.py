# Initializes package called app, containing routes.py

from flask import Flask

app = Flask(__name__)

from app import routes
