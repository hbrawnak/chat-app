from flask import Flask, render_template, request, redirect, url_for, jsonify
from . import auth
from . import login_required

app = Flask(__name__, template_folder='templates')
app.secret_key = "FvigywQvsF6D2Yc"


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
            return redirect(url_for('home'))
    else:
        return render_template('login.html')


@app.route('/chat', methods=['GET', 'POST'])
@login_required
def chat():
    return render_template('chat.html')


@app.route('/info', methods=['GET', 'POST'])
@login_required
def info():
    return render_template('info.html')


@app.route('/logout', methods=['GET'])
@login_required
def logout():
    auth.logout()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
