from flask import Flask

myproject = Flask(__name__)

myproject.config.from_object("config.DevelopmentConfig")

from myproject import views
