from flask import redirect, url_for
from functools import wraps
from .auth import logged_in


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if logged_in():
            return f(*args, **kwargs)
        else:
            return redirect(url_for('home'))

    return wrap
