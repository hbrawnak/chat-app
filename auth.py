from flask import session
from . import db

db = db.db_connection()


def set_user(username):
    if not _user_is_exist(username):
        register(username=username)
        set_user_session(username=username)
    else:
        login(username=username)

    return get_user_session()


def login(username):
    set_user_session(username=username)


def register(username):
    return db.users.insert_one({"username": username, "isActive": True})


def logout():
    session.pop('user', None)


def _user_is_exist(username):
    return db.users.find_one({"username": username})


def set_user_session(username):
    session['user'] = username


def get_user_session():
    return session.get('user')


def set_user_inactive():
    pass


def set_user_active():
    pass


def logged_in():
    if not get_user_session():
        return False
    else:
        return True
