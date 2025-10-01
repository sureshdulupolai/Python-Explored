from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import db
from app.models import Task
from functools import wraps

tasks_bp = Blueprint('tasks', __name__)

# Login check decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

@tasks_bp.route("/")
@login_required
def view_tasks():
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)

@tasks_bp.route("/add", methods=["POST"])
@login_required
def add_task():
    title = request.form.get('title')
    if title:
        new_task = Task(title=title, status='Pending')
        db.session.add(new_task)
        db.session.commit()
        flash("Task Added Successfully", "success")
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route("/toggle/<int:task_id>/", methods=["POST"])
@login_required
def toggle_status(task_id):
    task = Task.query.get(task_id)
    if task:
        if task.status == "Pending":
            task.status = "Working"
        elif task.status == "Working":
            task.status = "Done"
        else:
            task.status = "Pending"
        db.session.commit()
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route("/clear", methods=["POST"])
@login_required
def clear_tasks():
    Task.query.delete()
    db.session.commit()
    flash('All tasks cleared!', 'info')
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/delete/<int:task_id>/', methods=["POST"])
@login_required
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        flash(f"Deleted Task ID: {task_id}", "info")
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route("/filter/<status>")
@login_required
def filter_tasks(status):
    if status == "all":
        tasks = Task.query.all()
    else:
        tasks = Task.query.filter_by(status=status.capitalize()).all()
    return render_template("tasks.html", tasks=tasks, filter_status=status)
