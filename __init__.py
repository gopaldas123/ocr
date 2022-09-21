from flask import Flask

ap = Flask(__name__)

ap.config.from_object("config.DevelopmentConfig")

from app import views
