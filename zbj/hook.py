#!/usr/bin/env python
# encoding: utf-8

"""
@file: hook.py
@time: 2016/8/25 23:33
@author: chenfan
"""
from flask import Flask,request
import json

app = Flask(__name__)

@app.route('/',methods=['POST'])
def index():
    data = request.args['token']
    data1 = request.data
    print data,data1
    return 'ok'
if __name__ == '__main__':
    app.run()