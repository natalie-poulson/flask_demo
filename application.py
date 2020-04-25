# import datetime

from flask import Flask, render_template

app = Flask(__name__)

#  Intial Practice
# @app.route('/')
# def index():
#     return 'Hello, world!'

# @app.route('/nat')
# def nat():
#     return 'Hello, nat!'

# @app.route('/<string:name>')
# def hello(name):
#     name = name.capitalize()
#     return f'<h1>Hello, {name}!<h2>'

# Templates & Variables
# @app.route('/')
# def index():
#     headline = 'Hello!'
#     return render_template('index.html', headline=headline)

# @app.route('/bye')
# def bye():
#     headline = 'See ya'
#     return render_template('index.html', headline=headline)


# Conditions
# @app.route('/')
# def index():
#     now = datetime.datetime.now()
#     anniversary = now.month == 2 and now.day == 20
#     return render_template('index.html', anniversary=anniversary)

# Loops
# @app.route('/')
# def index():
#     names = ['Alice', 'Bob', 'Charlie']
#     return render_template('index.html', names=names)

# URLs & Links
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/more')
def more():
    return render_template('more.html')