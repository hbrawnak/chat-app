from model.user import User
from service.helper import remove_user_session, set_user_session, get_user_session


def set_user(username):
    if not _user_is_exist(username):
        register(username=username)
        set_user_session(username=username)
    else:
        login(username=username)

    return get_user_session()


def login(username):
    set_user_session(username=username)
    set_user_active(username)


def register(username):
    return User(username=username).save_one()


def logout():
    set_user_inactive(get_user_session())
    remove_user_session()


def _user_is_exist(username):
    return User.find_one({"username": username})


def set_user_inactive(username):
    return User.update_one(where_key_value={"username": username}, set_key_value={"isActive": False})


def set_user_active(username):
    return User.update_one(where_key_value={"username": username}, set_key_value={"isActive": True})


def logged_in():
    return True if get_user_session() else False
