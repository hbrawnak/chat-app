from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_socketio import SocketIO, join_room, emit, send

from . import auth, login_required
from .helper import get_chat_room_active_users

app = Flask(__name__, template_folder='templates')
app.secret_key = "FvigywQvsF6D2Yc"

socketio = SocketIO(app, manage_session=False)
room_name = 'chatapp'


@app.route('/', methods=['GET', 'POST'])
def home():
    if auth.logged_in():
        return redirect(url_for('chat'))

    if request.method == 'POST':
        try:
            r = request.form['username']
            if r:
                auth.set_user(r)
                return redirect(url_for('chat'))
            else:
                return redirect(url_for('home'))
        except Exception as e:
            print(str(e))
            return redirect(url_for('home'))
    else:
        return render_template('login.html')


@app.route('/chat', methods=['GET', 'POST'])
@login_required
def chat():
    return render_template('chat.html', user=auth.get_user_session())


@app.route('/info', methods=['GET', 'POST'])
@login_required
def info():
    users = get_chat_room_active_users()
    return render_template('info.html', users=users)


@app.route('/logout', methods=['GET'])
@login_required
def logout():
    auth.logout()
    return redirect(url_for('home'))

#
# @socketio.on('join', namespace='/chat')
# def join(message):
#     room = room_name
#     payload = {'user': auth.get_user_session(), 'msg': auth.get_user_session() + ' has entered the room.',
#                'type': 'status'}
#     join_room(room)
#     emit('status', payload, room=room)
#
#
# @socketio.on('text', namespace='/chat')
# def text(message):
#     room = room_name
#     emit('message', {'msg': auth.get_user_session() + ' : ' + message['msg']}, room=room)


@app.route('/ping', methods=['POST'])
def ping():
    if request.method == 'POST':
        room = room_name
        payload = {'user': auth.get_user_session(), 'msg': request.form['msg'], 'type': 'message'}
        emit('message', payload, room=room, namespace='/chat', broadcast=True)
        return jsonify({"status": "okay"})

    return jsonify({"status": False})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    socketio.run(app)
