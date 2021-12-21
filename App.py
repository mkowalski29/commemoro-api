from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return"Welcome to the Commemoro API. Current Version 0.0.1; Author: Maggie"

@app.route('/profile', methods=['GET'])
def profile():
    """"Accepts a User Id and returns the users profile"""
    # Need to define a users profile (Maggie)
    # GET: Paramater of the User Id
    # RETURNS: JSON User ID
    # POST: Create profile
    # PUT: Allow us to update the users profile
    return "Profile is coming soon!"

@app.route('/saved_locations', methods=['GET'])
def saved_locations():
    """Manages users saved locations"""
    # POST: Create and Retrieve Locations
    # PUT: Update a saved location
    # DELETE: Remove a saved location
    return "Locations are also coming soon"




# Needed Routes
#1 - Show user profile
#2 - Show user's saved locations
#3 - Search for Locations (Maybe)
#4 - Save a location
#5 - Delete a location

