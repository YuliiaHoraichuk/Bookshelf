class User:
    def __init__(self):
        self.current_user = None
        self.users = {}

# BASIC SIGNUP FUNCTIONALITY - TO BE UPDATED
    def create_user(self, username, password):
        if username in self.users:
            return False, "Username already exists"
        else:
            self.users[username] = {"password": password}
            return True, "User created successfully"