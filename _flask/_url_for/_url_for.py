#coding: utf-8

from flask import Flask, url_for

"""
@file: _url_for.py
@time: 2017/8/31 
@author: chenfan
"""

app = Flask(__name__)

@app.route('/index',strict_slashes=False)
#strict_slashes使得/index与/index/都正常
def index():
    return "index"

@app.route('/about/')
def about():
    return "about"

@app.route('/user/<name>')
def user(name):
    return name

with app.test_request_context():
    print url_for("index")
    print url_for("user", name='tom jk')

if __name__ == "__main__":
    app.debug = True
    app.run()