from flask import Flask, jsonify

# Dictionary of Justice League
justice_league_members = [
    {"superhero": "Aquaman", "real_name": "Arthur Curry"},
    {"superhero": "Batman", "real_name": "Bruce Wayne"},
    {"superhero": "Cyborg", "real_name": "Victor Stone"},
    {"superhero": "Flash", "real_name": "Barry Allen"},
    {"superhero": "Green Lantern", "real_name": "Hal Jordan"},
    {"superhero": "Superman", "real_name": "Clark Kent/Kal-El"},
    {"superhero": "Wonder Woman", "real_name": "Princess Diana"}
]

#################################################
# Flask Setup
# create app
app = Flask(__name__)

# Create a dictionary
my_dict = {"name": "Justice League Members"}


#################################################
# @TODO: Initialize your Flask app here
# YOUR CODE GOES HERE

#################################################
# Flask Routes
#################################################

# @TODO: Complete the routes for your app here
# YOUR CODE GOES HERE

# let's create a home route
@app.route("/")
def home():
    return "Hello, this is a site for the Justice League"

# Create route "Normal"
@app.route("/members")
def members():
    return f"Our membership includes justice_league_members}."

# Create josonified route

@app.route("/api/v1.0/justice-league")
def jsonified():
    return jsonify(justice_league_members)

# Boiler plate

if __name__ == "__main__":
    # @TODO: Create your app.run statement here
    app.run(debug=True) # Production environment should be false.
