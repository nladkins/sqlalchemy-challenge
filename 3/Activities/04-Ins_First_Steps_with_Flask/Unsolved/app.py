# Import Flask
from flask import Flask

# Create app name
app = Flask(__name__)

# Define what to do whent a user hits the index route.
@app.route("/")
def home():
    print("Creating a home page")
    return "This is my first flask app"

# Create a route page
@app.route("/about")
def about():
    print("Creating an about page")
    return "This is about me."

# Get the app to start to run.
if __name__ == '__main__':
    app.run(debug=True) # Production environment should be false.