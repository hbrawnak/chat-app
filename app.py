from flask import Flask, render_template, request, redirect, url_for, jsonify
from . import auth

app = Flask(__name__, template_folder='templates')
app.secret_key = "FvigywQvsF6D2Yc"


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            r = request.form['username']
            if r:
                auth.set_user(r)
                return redirect(url_for('chat'))
            else:
                return redirect(url_for('home'))
        except Exception as e:
            return redirect(url_for('home'))
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
