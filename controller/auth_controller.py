from model.user_auth import User

class AuthController:
    def __init__(self, app):
        self.app = app
        self.user = User()

# WRITE ACTUAL FUNCTION LATER
    def handle_login(self, username, password):
        print(username, password)