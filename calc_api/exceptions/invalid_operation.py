from flask import jsonify

# Define Invalid Operation class to be used on response errors.
class InvalidOperation(Exception):
    status_code = 400 # Bad Request

    # Default constructor of exception class
    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        self.payload = payload
    
        if status_code is not None:
            self.status_code = status_code

    # transform invalid operator exception into map object.
    def to_dict(self):
        invalid_operation = dict(self.payload or ())
        invalid_operation['message'] = self.message
        return invalid_operation