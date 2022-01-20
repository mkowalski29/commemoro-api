from flask import Flask, request, jsonify
from user import User
from location import Location

app = Flask(__name__)

@app.route('/')
def index():
    return"Welcome to the Commemoro API. Current Version 0.0.1; Author: Maggie"

@app.route('/profile', methods=['GET'])
def profile():
    id = request.args.get('id')
    user = User(id)
    user_profile = user.get_user_profile()

@app.route('/saved_locations', methods=['GET'])
def saved_locations():
    id = request.args.get('id')
    locations = Location(id)
    user_locations = locations.get_saved_locations()

    return user_locations


