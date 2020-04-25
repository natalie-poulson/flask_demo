from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/nat')
def nat():
    return 'Hello, nat!'