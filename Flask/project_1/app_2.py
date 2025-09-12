from flask import Flask, render_template

app = Flask(__name__)

# jinja2 =>. template rendering some data
@app.route("/")
def home():
    return render_template('profile.html',
        name="Suresh",
        is_topper=True,
        subjects=["Maths", "Python", "Django", "Flask"]
    )
    