# Import Flask
from flask import Flask

# Create app name
app = Flask(__name__)

# Define what to do whent a user hits the index route.
@app.route("/")
def home():
    print("Welcome to my API")
    return "Hello class, this is Norman's App"

# Create a about page
@app.route("/about")
def about():
    print("About Me")
    return "In case you didn't know, I live in Fuquay Varina, NC."

# Create a route page
@app.route("/contact")
def contact():
    print("Contact Me")
    return "You all can reach me at do_not_email_me_again@yahoo.com"

# Get the app to start to run.
if __name__ == '__main__':
    app.run(debug=True) # Production environment should be false.