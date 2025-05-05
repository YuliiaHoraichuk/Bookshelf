import customtkinter as ctk
from config import ACCENT_COLOR_1, ACCENT_COLOR_2, ACCENT_COLOR_3, BACKGROUND_COLOR
from view.login_display import InputFrame

class SignupDisplay(ctk.CTkFrame):
    def __init__(self, parent, auth_controller, **kwargs):
        super().__init__(parent, **kwargs)

# Frame: Login and Password input fields
        self.input_frame = InputFrame(self, fg_color=ACCENT_COLOR_3, border_color=ACCENT_COLOR_1, border_width=2)
        self.input_frame.grid(row=3, column=0, columnspan=2, pady=20, sticky="nsew")

# Label: Welcome message
        self.welcome_message = ctk.CTkLabel(self, text="Welcome to the Bookshelf App!", font=("Garamond", 28, "bold"),
                                            text_color=ACCENT_COLOR_1)
        self.welcome_message.grid(row=0, column=0, columnspan=2, pady=(160,0))

# Label: Error message ROW 1 -- normally hidden
        self.error_message = ctk.CTkLabel(self, text="") # ADD ERROR TXT LATER
        self.error_message.grid(row=1, column=1, padx=20, pady=10)
        self.error_message.grid_forget()