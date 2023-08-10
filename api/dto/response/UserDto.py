class UserDto: 
    id = 0
    email = ""
    username  = ""
    lastName  = ""
    firstName = ""

    def __init__(self, data):
        print("dot triger=====", data)
        self.validators()
      
    def validators(self): 
        return ["error"]


#     import pydantic
# class UserDto(pydantic.BaseModel):
#   name: str
#   email: pydantic.EmailStr
#   age: int
  
#   @pydantic.validator("age")
#   def validate_age(cls, age):
#     if age < 18:
#       raise ValueError("Age must be at least 18")

# def validate_user_request(request):
#   """Validates the data in the user request."""

#   user_dto = UserDto.parse_obj(request.get_json())
#   user_dto.validate()

#   return user_dto
