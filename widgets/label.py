from tkinter import Label as TkLabel


class Label(TkLabel):
    def __init__(self, master=None, **kwargs):
        super().__init__(master=master, **kwargs)

    def set_text(self, text):
        self.config(text=text)
