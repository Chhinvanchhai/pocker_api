
from api.dto.response.UserDto import UserDto
from api.services.UserSerivce import UserService
from api.shared.Utils import Utils, Validator
from flask import request
# from wtforms import Form , StringField, PasswordField, validators

# class RegistrationForm(Form):
#     username = StringField(self.request.form, [validators.Length(min=4, max=25)])
#     email = StringField('Email Address', [validators.Length(min=6, max=35)])
#     password = PasswordField('New Password', [
#         validators.DataRequired(),
#         validators.EqualTo('confirm', message='Passwords must match')
#     ])

class UserController(Utils): 
    def __init__(self, userService):
      self.userService = userService

    def users(self):
        req = UserDto(request.json)
        print("request=====", req)
        try:
            if request.method == 'POST':
                if not self.isEmail(request.json['email']):
                    return self.validationResponse(500,400, 'failed validation' ,["email is invalide!"])
                
                return self.userService.store(request.json)
            else:
                listUser =  self.userService.users()
                data = []
                for row in listUser:
                    data.append({
                        "id": row.id,
                        "email": row.email,
                        "username": row.username,
                        "lastName": row.lastName,
                        "firstName": row.firstName
                    })
                return self.Response(200,200, 'Success', data)
        except Exception as e:
            return self.Response(400,400, str(e), {})

    def get(self,id):
        return  self.userService.get(id)

    def update(self, id):
        return  self.userService.update(id, request.json)

    def delete(self, id):
        return  self.userService.delete(id)