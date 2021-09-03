from flask import session

from model.message import Message
from model.user import User


def get_chat_room_active_users():
    return User.find_all(where_key_value={"isActive": True})


def save_message(text, user):
    message = Message(text, user)
    return message.save_one()


def get_messages():
    return Message.find_all(sort_desc='created_at', limit=50)


def set_user_session(username):
    session['user'] = username


def get_user_session():
    return session.get('user')


def remove_user_session():
    session.pop('user', None)
