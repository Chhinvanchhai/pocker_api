
from flask import jsonify, make_response
from api.config.db import Roles, db, User, engine, Address
from api.dto.response.UserDto import UserDto
from api.shared.Utils import FailedHanlde
from sqlalchemy import delete, select, update, asc
from sqlalchemy.orm import Session

class UserService: 

    def __init__(self):
        self.session = Session(engine)
    
    def users(self):
        try: 
            # users = db.query(User).join(Address, isouter= True).order_by(User.id.asc()).filter(User.id > 50)
            # return users
            # query = db.query(User).order_by(User.id).filter(User.id > 5)
            query =  db.query(User).join(Roles, isouter= True ).join(Address, isouter= True).order_by(User.id.asc())
            page = 1
            per_page = 3
            results = query.limit(per_page).offset((page - 1) * per_page).all()
            return results
        except Exception as e:
            return f"An exception occurred: {str(e)}"
        

    
    def get(self,id):
        user = db.get(User,id)
        if(not user):
            return make_response(jsonify({"status": "Not found"}), 200)
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
        print("data =====", data)
        try:
            user = User(
                email=data['email'],
                password=data['password'],
                username=data['username'],
                lastName=data['lastName'],
                firstName=data['firstName'],
                status=data['status'],
            )
            db.add(user)
            db.commit()
            json = {
                    "status": True,
                    "message": "Added Successfull"
            }
            return make_response(jsonify(json), 200)
        except FailedHanlde as e:
            db.rollback()
            return str(e)
        finally:
            db.close()

    def update(self, id, data):
        stmt = (
            update(User).
            where(User.id == id).
            values(lastName=data['lastName'],firstName = data['firstName'])
        )


        try:
            db.execute(stmt)
            json = {
                "status": True,
                "message": "Update Successfull"
            }
            return make_response(jsonify(json), 201)
        except:
            return "error"
    
    def delete(self, id):
        db.execute(delete(User).where(User.id == id))
        # db.commit()
        # User.delete().where(User.id == id)
        json = {
            "status": True,
            "message": "Delete Successfull"
        }
        return make_response(jsonify(json), 200)