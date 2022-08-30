from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return 'modified file'

@app.route('/index1')
def index1():
    return 'modified file' ## API 1

@app.route('/index2')
def index2():
    return 'modified file' ## API 2

@app.route('/index2')
def index2():
    return 'modified file' ## API 3

