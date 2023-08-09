
from flask import jsonify, make_response
from api.config.db import db, User
from api.dto.response.UserDto import UserDto
from api.shared.Utils import FailedHanlde
    
class UserService: 

    
    
    def users(self):
        try: 
            users = User.query.all()
            return users
        except Exception as e:
            return f"An exception occurred: {str(e)}"
        
    
    def get(self,id):
        user = User.query.get_or_404(id)
        json = {
            "status": True,
            "data": {
                "id": user.id,
                "email": user.email,
                "username": user.username,
                "lastName": user.lastName,
                "firstName": user.firstName
            }
        }
        return make_response(jsonify(json), 200)
    
    def store(self,  data):
        try:
            user = User(
                email=data['email'],
                password=data['password'],
                username=data['username'],
                lastName=data['lastName'],
                firstName=data['firstName'],
                status=data['status'],
            )
            db.session.add(user)
            db.session.commit()
            json = {
                    "status": True,
                    "message": "Added Successfull"
            }
            return make_response(jsonify(json), 200)
        except FailedHanlde as e:
            return str(e)

    def update(self, id, data):
        user = User.query.get_or_404(id)
        user.lastName = data['lastName']
        user.firstName = data['firstName']
        user.username = data['username']

        try:
            db.session.commit()
            json = {
                "status": True,
                "message": "Update Successfull"
            }
            return make_response(jsonify(json), 201)
        except:
            return "error"
    
    def delete(self, id):
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        json = {
            "status": True,
            "message": "Delete Successfull"
        }
        return make_response(jsonify(json), 200)