from flask import jsonify, make_response
import re

class Utils: 
    def Response(self,statusCode, code, status, data):
        json = {
            "status": status,
            "code": code,
            "data": data
        }
        return make_response(jsonify(json), statusCode)
    
    def validationResponse(self,statusCode, code, messages):
        json = {
            "code": code,
            "messages": messages
        }
        return make_response(jsonify(json), statusCode)
    
    def isEmail(self, email):
        regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+$"
        if re.match(regex, email):
            return True
        else:
            return False
    

class FailedHanlde(Exception):
    def __init__(self, m):
        self.message = m
    def __str__(self):
        return self.message
    

class Validator:
    def __init__(self):
        pass

    def validate_email(email):
        regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+$"
        if re.match(regex, email):
            return True
        else:
            return False