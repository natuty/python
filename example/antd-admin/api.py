#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/api/v1/user/login', methods=['GET', 'POST'])
def login():
    return '{"status":true}'

@app.route('/api/user', methods=['GET', 'POST'])
def user():
    return '<h1>user</h1>'
@app.route('/', methods=['GET', 'POST'])
def index():
    return '<h1>antd-admin</h1>'

if __name__ == '__main__':
    app.run(host="localhost",port=8888,debug=True)
