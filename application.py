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

# Working with HTML files
@app.route('/')
def index():
    headline = 'Hello!'
    return render_template('index.html', headline=headline)

@app.route('/bye')
def bye():
    headline = 'See ya'
    return render_template('index.html', headline=headline)