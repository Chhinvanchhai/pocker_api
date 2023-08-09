class User: 
    username = ""
    email = ""
    lastName = ""
    firstName = ""
    createdAt = ""
    status = 0

    def __init__(self, username, email, lastName, firstName, createdAt, status):
        self.username = username
        self.email = email,
        self.lastName = lastName
        self.firstName = firstName
        self.createdAt = createdAt
        self.status = status        