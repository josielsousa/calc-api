#!/usr/bin/env python3

from flask import Flask

# define aplication using Flask framework.
app = Flask(__name__)

@app.route('/')
def home():
    return 'api is up...'

@app.route('/calculate/<operation>/<num1>/<num2>')
def calculate(operation, num1, num2):
    return 'aaaa'

# checks to see if name of the package is main package.
if __name__ == '__main__':
    app.run()