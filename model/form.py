from flask_wtf import FlaskForm
from wtforms import StringField

from services.auth import set_user


class LoginForm(FlaskForm):
    username = StringField('username')

    @staticmethod
    def save(username):
        return set_user(username)

    @staticmethod
    def check_len(username):
        if len(username) > 20:
            return False
        elif len(username) < 4:
            return False
        else:
            return True
