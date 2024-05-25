from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/services')
def services():
    return '<h1>Services Page</h1>'

@app.route('/contacts')
def index():
    title = 'Welcome to my contacts page!'
    message = 'This is an example of using Flask templates.'
    return render_template('index.html', title=title, message=message)

