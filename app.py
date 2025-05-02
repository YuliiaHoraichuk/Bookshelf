import customtkinter as ctk
from view.login_display import LoginDisplay
from controller.auth_controller import AuthController
from config import BACKGROUND_COLOR

# Main app controller
class BookshelfApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Bookshelf App")
        self.geometry("1000x700")
        self.minsize(400,500)
        self.configure(fg_color=BACKGROUND_COLOR)

        self.current_frame = None

        self.auth_controller = AuthController(self)

# Load login display on launch
        self.show_login()

# Switch between frames
    def switch_frame(self, frame, fill_space):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = frame(self, auth_controller=self.auth_controller,fg_color=BACKGROUND_COLOR)
        self.current_frame.grid(row=0, column=0, sticky=fill_space)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

# Switch display to login
    def show_login(self):
        self.switch_frame(LoginDisplay, "ns")

    #def show_signup(self):
    #    self.switch_frame()


app = BookshelfApp()
app.mainloop()