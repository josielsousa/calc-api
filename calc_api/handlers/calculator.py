from flask import Blueprint, jsonify
from calc_api.common.calc import calculate, has_operation, operations
from calc_api.exceptions.invalid_operation import InvalidOperation

# define Blueprint for calculator handler.
calculator_handler = Blueprint('calculator_handler', __name__, root_path='/calculator')

# returns an map of operations available.
@calculator_handler.route('/calculator/operations', methods=['GET'])
def get_operations():
    return operations

# define a calculate router to execute a operation.
@calculator_handler.route('/calculator/<operation>/<int:num1>/<int:num2>')
def calc(operation, num1, num2):
    result = ''
    if not has_operation(operation):
        msg = 'operation [{}] not found'.format(operation)
        raise InvalidOperation(msg)
    else:
        result = calculate(operation, num1, num2)
    return result


# define any route with exception.
@calculator_handler.route('/foo')
def get_foo():
    raise InvalidOperation('This view is gone', status_code=403)

# register handle function to handle a InvalidOperation exception.
@calculator_handler.errorhandler(InvalidOperation)
def handle_invalid_operation(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
