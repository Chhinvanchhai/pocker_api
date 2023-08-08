
from flask import jsonify, make_response
from api.config.db import db, User
class UserService: 
    
    def users(self):
        users = User.query.all()
        json = {
            "status": True,
            "data": []
        }
        for row in users:
            json['data'].append({
                "id": row.id,
                "email": row.email,
                "username": row.username,
                "lastName": row.lastName,
                "firstName": row.firstName
            })
            print(row.username)
        return make_response(jsonify(json), 200)
        
    
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
    
    def store(self, data):
        user = User(
            email=data['email'],
            password=data['password'],
            username=data['username']
        )
        db.session.add(user)
        db.session.commit()
        json = {
                "status": True,
                "message": "Added Successfull"
        }
        return make_response(jsonify(json), 200)

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