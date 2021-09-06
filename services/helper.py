from flask import session

from model.message import Message
from model.user import User


def get_chat_room_active_users():
    """ Chat Room active user list """
    return User.find_all(where_key_value={"isActive": True})


def save_message(text, user):
    """ Save a single message """
    message = Message(text, user)
    return message.save_one()


def get_messages():
    """ Find last 100 messages """
    return Message.find_all(sort_desc="created_at", limit=100)


def set_user_session(username):
    """ Set current user session """
    session["user"] = username
    return get_user_session()


def get_user_session():
    """ Get current user session """
    return session.get("user")


def remove_user_session():
    """ Remove current user session """
    return session.pop("user", None)
