import logging
import os
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from flask_socketio import SocketIO, join_room, leave_room, emit
from datetime import datetime

from services.auth import logged_in, get_user_session, logout as user_logout
from services.helper import get_chat_room_active_users, get_messages
from services.worker import queue_worker as message_queue

from model.form import LoginForm

from . import login_required

app = Flask(__name__, template_folder='templates')
socketio = SocketIO(app, manage_session=False)

app.secret_key = os.getenv('APP_SECRET')
room_name = os.getenv('APP_NAME')


@app.route('/', methods=['GET', 'POST'])
def home():
    """ Render login page without session. If session redirect to chat page """
    if logged_in():
        return redirect(url_for('chat'))

    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        try:
            r = form.username.data

            if not form.check_len(r):
                flash('Username should be within 4 to 20 characters')
                return redirect(url_for('home'))

            if form.save(r):
                return redirect(url_for('chat'))
            else:
                return redirect(url_for('home'))

        except Exception as e:
            logging.error(str(e))
            return redirect(url_for('home'))
    else:
        return render_template('login.html', form=form)


@app.route('/chat', methods=['GET', 'POST'])
@login_required
def chat():
    """ Render chat page for logged in users """
    return render_template('chat.html', user=get_user_session(), messages=get_messages())


@app.route('/info', methods=['GET', 'POST'])
@login_required
def info():
    """ Render info page fpr showing user list in chat room """
    users = get_chat_room_active_users()
    return render_template('info.html', users=users)


@app.route('/logout', methods=['GET'])
@login_required
def logout():
    """ Logout current user and redirect to login """
    user_logout()
    return redirect(url_for('home'))


@socketio.on('join', namespace='/chat')
def join(message):
    """ On Joining Socket """
    join_room(room_name)


@socketio.on('left', namespace='/chat')
def left(message):
    """ On Leaving Socket """
    leave_room(room_name)


@app.route('/message', methods=['POST'])
@login_required
def message():
    """ Receive message from API request """
    if request.method == 'POST':
        room = room_name
        user = get_user_session()
        msg = request.form['msg']

        # Message broadcasting through socket
        time = datetime.now().strftime('%I:%M %p')
        payload = {'user': user, 'msg': user + ': ' + request.form['msg'], 'create_at': time}
        emit('message', payload, room=room, namespace='/chat', broadcast=True)

        # Sending message to queue for saving
        message_queue(msg, user)
        return jsonify({'status': True})

    return jsonify({'status': False})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
    socketio.run(app)
