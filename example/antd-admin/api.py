#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/api/user/login', methods=['GET', 'POST'])
def login():
    return '{"status":true}'

@app.route('/api/user', methods=['GET', 'POST'])
def user():
    return '<h1>user</h1>'

if __name__ == '__main__':
    app.run(host="localhost",port=9000)
