import customtkinter as ctk
from config import ACCENT_COLOR_1, ACCENT_COLOR_2, ACCENT_COLOR_3, BACKGROUND_COLOR


class LoginDisplay(ctk.CTkFrame):
    def __init__(self, parent, main_controller, auth_controller, **kwargs):
        super().__init__(parent, **kwargs)

        self.main_controller = main_controller
        self.auth_controller = auth_controller

# Label: Welcome message
        self.welcome_message = ctk.CTkLabel(self, text="Welcome to the Bookshelf App!", font=("Garamond", 28, "bold"),
                                            text_color=ACCENT_COLOR_1)
        self.welcome_message.grid(row=0, column=0, columnspan=2, pady=(130,0))

# Label: Error message ROW 1 -- normally hidden
        self.error_message = ctk.CTkLabel(self, text="") # ADD ERROR TXT LATER
        self.error_message.grid(row=1, column=1, padx=20, pady=10)
        self.error_message.grid_forget()

# Frame: Switch between the LOGIN / SIGNUP frames
        self.button_switch_frame = ctk.CTkFrame(self, fg_color=BACKGROUND_COLOR)
        self.button_switch_frame.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")

        self.button_switch_frame.columnconfigure(0, weight=1)
        self.button_switch_frame.columnconfigure(1, weight=1)

# Button: Switch to the Login frame
        self.switch_to_login = ctk.CTkButton(self.button_switch_frame, width=150, height=50, text="Log In",
                                             font=("Arial", 18), text_color="#fff",
                                             fg_color=ACCENT_COLOR_1, hover_color=ACCENT_COLOR_1,
                                             corner_radius=2, command="") # ADD COMMAND LATER
        self.switch_to_login.grid(row=0, column=0, pady=(50,0), sticky="ew")

# Button: Switch to the Signup frame
        self.switch_to_signup = ctk.CTkButton(self.button_switch_frame, width=150, height=50, text="Sign Up",
                                              font=("Arial", 18), text_color=ACCENT_COLOR_1,
                                              fg_color=BACKGROUND_COLOR, hover_color=ACCENT_COLOR_3,
                                              border_color=ACCENT_COLOR_1, border_width=2,
                                              corner_radius=2, command=self.main_controller.show_signup)
        self.switch_to_signup.grid(row=0, column=1, pady=(50,0), sticky="ew")

# Frame: Login and Password input fields
        self.input_frame = InputFrame(self, fg_color=ACCENT_COLOR_3, border_color=ACCENT_COLOR_1, border_width=2)
        self.input_frame.grid(row=3, column=0, columnspan=2, pady=20, sticky="nsew")

# Button: Log In
        self.login_button = ctk.CTkButton(self, width=150, height=50, text="Log In", font=("Arial", 18),
                                          fg_color=ACCENT_COLOR_1, hover_color=ACCENT_COLOR_2,
                                          text_color="#fff", corner_radius=25,
                                          command="") # ADD COMMAND LATER
        self.login_button.grid(row=4, column=0, columnspan=2, pady=20, sticky="ew")

# Pass username and password to the auth_controller
    def login(self):
        self.auth_controller.handle_login(self.input_frame.get_credentials())


# Frame: Login and Password input fields
class InputFrame(ctk.CTkFrame):
    def __init__(self, parent, include_confirm_password=False, **kwargs):
        super().__init__(parent, **kwargs)

# 2 columns: label and input
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=5)

# Username label and input
        # Label
        self.username_label = ctk.CTkLabel(self, text="Username:", font=("Arial", 20), text_color=ACCENT_COLOR_1)
        self.username_label.grid(row=0, column=0, padx=(30,0), pady=(30,10), sticky="w")

        # Input
        self.username_input = ctk.CTkEntry(self, font=("Arial", 18), corner_radius=25,
                                           border_color=ACCENT_COLOR_1,
                                           fg_color=BACKGROUND_COLOR)
        self.username_input.grid(row=0, column=1, ipady=3, padx=(0,30), pady=(30,10), sticky="ew")

# Password label and input
        # Label
        self.password_label = ctk.CTkLabel(self, text="Password:", font=("Arial", 20), text_color=ACCENT_COLOR_1)
        self.password_label.grid(row=1, column=0, padx=(30,0), pady=(10,30), sticky="w")

        # Input
        self.password_input = ctk.CTkEntry(self, font=("Arial", 18), show="*", corner_radius=25,
                                           border_color=ACCENT_COLOR_1,
                                           fg_color=BACKGROUND_COLOR)
        self.password_input.grid(row=1, column=1, ipady=3, padx=(0,30), pady=(10,30), sticky="ew")

        if include_confirm_password:
            self.confirm_password_label = ctk.CTkLabel(self, text="Confirm Password:", font=("Arial", 20), text_color=ACCENT_COLOR_1)
            self.confirm_password_label.grid(row=2, column=0, padx=(30,0), pady=(10,30), sticky="w")

            self.confirm_password_input = ctk.CTkEntry(self, font=("Arial", 18), show="*", corner_radius=25, border_color=ACCENT_COLOR_1, fg_color=BACKGROUND_COLOR)
            self.confirm_password_input.grid(row=2, column=1, ipady=3, padx=(0,30), pady=(10,30), sticky="ew")

    def get_credentials(self):
        return self.username_input.get(), self.password_input.get()
