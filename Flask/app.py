# website brain
from flask import Flask, request

# set run this file
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello User! This is my first Flask App"

@app.route('/about')
def about():
    return "This is About Page in Flask"

@app.route("/submit_data", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        return "You Sent Data"
    else:
        return "You are only viewing form"

if __name__ == "__main__":
    app.run(debug=True)