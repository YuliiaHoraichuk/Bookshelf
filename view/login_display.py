import customtkinter as ctk

class LoginDisplay(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        #self.controller = controller

        self.columnconfigure(2, weight=1)

        self.welcome_message = ctk.CTkLabel(self, text="Welcome to the Bookshelf App!", font=("Helvetica", 16))
        self.welcome_message.grid(row=0, column=1, columnspan=2, pady=10)