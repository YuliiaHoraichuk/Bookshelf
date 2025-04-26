import customtkinter as ctk
from view.login_display import LoginDisplay

class BookshelfApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.current_frame = None

        self.login_frame = LoginDisplay(self)

        self.title("Bookshelf App")

# Load login display on launch
        self.switch_frame(self.login_frame)

    def switch_frame(self, frame):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = frame
        self.current_frame.grid()


app = BookshelfApp()
app.mainloop()