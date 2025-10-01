from flask import Blueprint, render_template, request, redirect, url_for, flash, session

auth_bp = Blueprint('auth', __name__)

# creating a dummy user like a non input user no user model
USER_CREDENTIALS = {
    "username" : 'admin',
    "password" : '1234'
}

@auth_bp.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
            session['user'] = username
            flash("Login Successful", "success")
            return redirect(url_for('tasks.view_tasks'))

        else:
            flash("Invalid username or password", 'danger')

    return render_template('login.html')

@auth_bp.route("/logout")
def logout():
    session.pop('user', None)
    flash("Logged out", "info")
    return redirect(url_for('auth.login'))

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Registration logic yaha
        username = request.form.get('username')
        password = request.form.get('password')
        flash(f"User {username} registered!", "success")
        return redirect(url_for('auth.login'))
    return render_template("register.html")
