import tkinter as tk

class Dropdown(tk.Frame):
    def __init__(self, master, options, command=None):
        super().__init__(master)
        self.master = master
        self.options = options
        self.command = command
        self.selected_option = tk.StringVar(self)

        self.dropdown = tk.OptionMenu(self, self.selected_option, *self.options, command=self._on_select)
        self.dropdown.pack(fill='both', expand=True)

    def _on_select(self, value):
        if self.command:
            self.command(value)

    def get_selected_option(self):
        return self.selected_option.get()

