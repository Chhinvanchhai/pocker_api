
class UserService: 
    
    def users(self):
        return "Listing  user"
    
    def get(self,id):
        return "get one  user:"+ str(id)
    
    def store(self, userDto):
        return "create user" + str(userDto)

    def update(self, id, data):
        return "update user: "+ str(id)
    
    def delete(self, id):
        return "delete user" + str(id)