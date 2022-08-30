from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return 'modified file'

@app.route('/new')
def indexy():
    return 'modified file new file added'