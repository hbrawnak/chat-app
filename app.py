import logging
import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_socketio import SocketIO, join_room, leave_room, emit
from datetime import datetime

from service.auth import logged_in, get_user_session, set_user, logout as user_logout
from service.helper import get_chat_room_active_users, get_messages
from service.worker import queue_worker as queue

from . import login_required

app = Flask(__name__, template_folder='templates')
socketio = SocketIO(app, manage_session=False)

app.secret_key = os.getenv('APP_SECRET')
room_name = os.getenv('APP_NAME')


@app.route('/', methods=['GET', 'POST'])
def home():
    if logged_in():
        return redirect(url_for('chat'))

    if request.method == 'POST':
        try:
            r = request.form['username']
            if r:
                set_user(r)
                return redirect(url_for('chat'))
            else:
                return redirect(url_for('home'))
        except Exception as e:
            logging.error(str(e))
            return redirect(url_for('home'))
    else:
        return render_template('login.html')


@app.route('/chat', methods=['GET', 'POST'])
@login_required
def chat():
    return render_template('chat.html', user=get_user_session(), messages=get_messages())


@app.route('/info', methods=['GET', 'POST'])
@login_required
def info():
    users = get_chat_room_active_users()
    return render_template('info.html', users=users)


@app.route('/logout', methods=['GET'])
@login_required
def logout():
    user_logout()
    return redirect(url_for('home'))


@socketio.on('join', namespace='/chat')
def join(message):
    join_room(room_name)


@socketio.on('left', namespace='/chat')
def left(message):
    leave_room(room_name)


@app.route('/message', methods=['POST'])
def message():
    if request.method == 'POST':
        room = room_name
        user = get_user_session()
        msg = request.form['msg']

        time = datetime.now().strftime('%I:%M %p')
        payload = {'user': user, 'msg': user + ': ' + request.form['msg'], 'create_at': time}
        emit('message', payload, room=room, namespace='/chat', broadcast=True)

        queue(msg, user)
        return jsonify({'status': True})

    return jsonify({'status': False})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    socketio.run(app)
