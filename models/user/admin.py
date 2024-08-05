from adt.user.base import WS_UserBase 

class WS_Admin:

    def __init__(self):
        self.id = 0
        self.name = ""
        self.password = ""
        self.role = "admin"
        self.chat_id = 0
        self.session = ""
    
    def authtenticate(self):
        return True

    def get_authentication_file(self, auth_name):
        auth_file = ""
        auth_dir = self.auth_dir()
        if auth_dir:
            auth_file = os.path.join(auth_dir, auth_name)
        return auth_file
