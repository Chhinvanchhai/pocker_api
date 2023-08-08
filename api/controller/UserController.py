
from api.dto.UserDto import UserDto
from api.services.UserSerivce import UserService
from flask import request


class UserController: 
    def __init__(self, userService):
      self.userService = userService

    def users(self):
        if request.method == 'POST':
            return self.userService.store(request.json)
        return  self.userService.users()

    def get(self,id):
        return  self.userService.get(id)

    def update(self, id):
        return  self.userService.update(id)

    def delete(self, id):
        return  self.userService.delete(id)