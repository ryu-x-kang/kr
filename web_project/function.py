from flask import render_template, redirect, session
from functools import wraps


def error(message):
    return render_template("error.html", message=message)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_email") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function
