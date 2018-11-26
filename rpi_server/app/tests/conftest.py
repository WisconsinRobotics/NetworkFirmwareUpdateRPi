import os
import tempfile
import sys
import pytest
import unittest
from flask import flash, Flask, request, redirect, render_template,  \
							 url_for, send_from_directory
sys.path.append('../../')
sys.path.append('../')
from app import app
import routes


@pytest.fixture
def app():
    """Create and configure a new app instance for each test.
    # create the app with common test config
    flask_app = Flask(__name__, instance_relative_config=True)
    flask_app.config['TESTING'] = True
"""
    yield routes.app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()
