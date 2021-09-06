from model.user import User
from services.helper import remove_user_session, set_user_session, get_user_session


def set_user(username):
    """ Register new user if not exist. If exist set user on session """
    if not _user_is_exist(username):
        register(username=username)
        set_user_session(username=username)
    else:
        login(username=username)

    return get_user_session()


def login(username):
    """ Login user and set active """
    set_user_session(username=username)
    return set_user_active(username)


def register(username):
    """ Register a new user """
    return User(username=username).save_one()


def logout():
    """ Logout current user and set inactive """
    set_user_inactive(get_user_session())
    return remove_user_session()


def _user_is_exist(username):
    """ Find user is exist or not """
    return User.find_one({"username": username})


def set_user_inactive(username):
    """ Set current user inactive """
    return User.update_one(where_key_value={"username": username}, set_key_value={"isActive": False})


def set_user_active(username):
    """ Set current user active """
    return User.update_one(where_key_value={"username": username}, set_key_value={"isActive": True})


def logged_in():
    """ User is exist on session or not """
    return True if get_user_session() else False
