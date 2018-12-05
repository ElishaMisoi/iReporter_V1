class Incident:
    # incident class
    def __init__(self, id, createdOn, createdBy, type, location,
                 status, Images, Videos, comment):
        self.id = id
        self.createdOn = createdOn
        self.createdBy = createdBy
        self.type = type
        self.location = location
        self.status = status
        self.Images = Images
        self.Videos = Videos
        self.comment = comment

    def get_incident(self):
        return {
            "id": self.id,
            "createdOn": self.createdOn,
            "createdBy": self.createdBy,
            "type": self.type,
            "location": self.location,
            "status": self.status,
            "Images": self.Images,
            "Videos": self.Videos,
            "comment": self.comment
        }

class User:
    # user class
    def __init__(self, id, firstname, lastname, othernames, email,
                 phoneNumber, username, registered, isAdmin, password, password_confirm):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.email = email
        self.phoneNumber = phoneNumber
        self.username = username
        self.registered = registered
        self.isAdmin = isAdmin
        self.password = password
        self.password_confirm = password_confirm

    def get_user_details(self):
        # getting one user
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "othernames": self.othernames,
            "email": self.email,
            "phoneNumber": self.phoneNumber,
            "username": self.username,
            "registered": self.registered,
            "isAdmin": self.isAdmin
        }
