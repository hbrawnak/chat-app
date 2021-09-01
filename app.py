from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from auth import login, register

app = Flask(__name__, template_folder='templates')

mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/todo_db")
db = mongodb_client.db

app.config["MONGO_URI"] = "mongodb://localhost:27017/chatapp"
mongodb_client = PyMongo(app)
db = mongodb_client.db


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            r = request.form['username']
            print(r)
            return redirect(url_for('chat'))
        except Exception as e:
            print(str(e))
            return redirect(url_for('/'))
    else:
        return render_template('login.html')


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    return render_template('chat.html')


@app.route('/info', methods=['GET', 'POST'])
def info():
    return render_template('info.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
