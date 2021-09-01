from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')


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


if __name__ == '__main__':
    app.run(debug=True)
