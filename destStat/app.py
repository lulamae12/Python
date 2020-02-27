from flask import Flask,render_template,request, session, Blueprint, redirect, url_for, request
import sys,datetime
import json

import flask_login
from flask_socketio import SocketIO

from termcolor import colored
from flask_basicauth import BasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)


socket = SocketIO(app)

@app.route("/")
def index():
    return render_template("home.html")


@app.route("/home")
def home():
    
    return render_template("home.html")





if __name__ == "__main__":
    
    app.run(debug=True)