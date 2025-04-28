import customtkinter as ctk

class LoginDisplay(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        #self.controller = controller

        self.columnconfigure(2, weight=1)

# Welcome message
        self.welcome_message = ctk.CTkLabel(self, text="Welcome to the Bookshelf App!", font=("Helvetica", 16))
        self.welcome_message.grid(row=0, column=1, columnspan=2, pady=10)

# Error message label ROW 1 -- normally hidden
        self.error_message = ctk.CTkLabel(self, text="") # ADD ERROR TXT LATER
        self.error_message.grid(row=1, column=1,padx=20, pady=10)
        self.error_message.grid_forget()

# Button: Switch frame to Log In
        self.switch_to_login = ctk.CTkButton(self, text="Log In", command="") # ADD COMMAND LATER
        self.switch_to_login.grid(row=2, column=1,padx=20, pady=10)

# Button: Switch frame to Sign Up
        self.switch_to_signup = ctk.CTkButton(self, text="Sign Up", command="") # ADD COMMAND LATER
        self.switch_to_signup.grid(row=2, column=2,padx=20, pady=10)

# Username label and input
        # Label
        self.username_label = ctk.CTkLabel(self, text="Username:")
        self.username_label.grid(row=3, column=1,padx=20, pady=10)
        # Input
        self.username_input = ctk.CTkEntry(self)
        self.username_input.grid(row=3, column=2, padx=20, pady=10)

# Password label and input
        # Label
        self.password_label = ctk.CTkLabel(self, text="Password:")
        self.password_label.grid(row=4, column=1,padx=20, pady=10)
        # Input
        self.password_input = ctk.CTkEntry(self, show="*")
        self.password_input.grid(row=4, column=2, padx=20, pady=10)

# Log In button
        self.login_button = ctk.CTkButton(self, text="Login", command="")
        self.login_button.grid(row=5, column=1, padx=20, pady=10)