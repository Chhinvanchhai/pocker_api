"""
 * @Author: Vanchhai
 * @Date: 2020-08-11 11:00:00
 * @Desciption: mapping route with plask and router
"""  

from api import app
from api.controller.AuthController import AuthController
from api.controller.UserController import UserController
from api.services.UserSerivce import UserService

userService  = UserService()
userController = UserController(userService)
authController = AuthController()

# user routing
@app.route('/users', methods = ['POST', 'GET'])
def users():   
  return  userController.users()

@app.route('/users/<int:id>', methods = ['GET'])
def get(id):
  return userController.get(id)

@app.route('/users/<int:id>/update', methods = ['POST'])
def update(id):
  return userController.update(id)

@app.route('/users/<int:id>', methods = ['DELETE'])
def delete(id):
  return userController.delete(id)

# auth routing
@app.route('/login', methods=['POST'])
def login():
  return authController.login()
