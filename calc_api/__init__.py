from flask import Flask, jsonify
from calc_api.handlers.calculator import calculator_handler

# initialize app with Flask framework.
app = Flask(__name__)

# declare handler calculator.
app.register_blueprint(calculator_handler)


# define home page, returning an message of success
@app.route('/')
def home():
    return 'api is up...'
