# Dependencies
from flask import Flask, jsonify

# create app
app = Flask(__name__)

# Create a dictionary
my_dict = {"name": "Norman"}

# let's create a home route
@app.route("/")
def home():
    return "Hello, this is my page"

# Create route "Normal"
@app.route("/normal")
def normal():
    return my_dict

# Create josonified route

@app.route("/jsonified")
def jsonified():
    return jsonify(my_dict)

# Boiler plate
if __name__ == '__main__':
    app.run(debug=True) # Production environment should be false.


