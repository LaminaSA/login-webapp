from flask import *

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/hello')
def hello():
    return render_template('hello.html')


@app.route('/about')
def about():
    return render_template('aboutme.html')


@app.route('/log', methods=['GET', 'POST'])
def log():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('hello'))
    return render_template('log.html', error=error)

@app.route('/test')
def test():
    return "Works!"

if __name__ == '__main__':
    app.run()
