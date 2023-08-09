from flask import abort, redirect, request, url_for
from api import app
class AuthController: 
   
    def login(selt):
        username = request.json['username']
        app.logger.info('%s logged in successfully', username)
        return "home"
        # if user.check_password(request.form['password']):
        
        #     return redirect(url_for('index'))
        # else:
        #     app.logger.info('%s failed to log in', user.username)
        #     abort(401)