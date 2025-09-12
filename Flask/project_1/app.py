from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    # render_template => search for folder by default as templates, inside that it search for home.html
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "suresh" and password == "123":
            return render_template("welcome.html", name = username)
        else:
            return render_template("login.html", error="Invalid credentials. Try again!")

    return render_template("login.html")

@app.route("/logout")
def logout():
    # Normally yaha session.clear() use hota hai, abhi simple message ke liye direct template render karte hain
    return render_template("logout.html")

@app.route("/profile")
def profile():
    return render_template('profile.html',
        name="Suresh",
        is_topper=True,
        subjects=["Maths", "Python", "Django", "Flask"]
    )
    

if __name__ == "__main__":
    app.run(debug=True)


