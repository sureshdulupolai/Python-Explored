from flask import Flask, request, redirect, url_for, session, Response


app = Flask(__name__)

# secret_key, this is important to set in flask when we use session, beacause other person can change session something 
# that why we need provide session_key, session lock
# if not use then flask dont provide session
app.secret_key = "supersecret"


# home page login
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":
            session["user"] = username # store in session
            return redirect(url_for("welcome"))

        else:
            # mimetype, what kind of thing to return for text send to HTMl
            return Response("In-Valid Credentials. Try Again", mimetype="text/plain")
        
    return """
        <h2>Login Page</h2>
        <form method="POST">
            Username: <input type="text" name="username"><br>
            Password: <input type="text" name="password"><br>
            <input type="submit" value="login">
        </form>
"""

@app.route("/welcome")
def welcome():
    if "user" in session:
        return f"""
        <h2>Welcome {session['user']}</h2>
        <a href={url_for('logout')}>Logout</a>
"""
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)