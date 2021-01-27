#!/usr/bin/python3
"""Module for Flask REST application."""
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv
from flask import make_response
