import tkinter as tk

class Button(tk.Button):
    def __init__(self, master, text="", command=None, bg="white", fg="black", width=None, height=None, **kwargs):
        super().__init__(master, text=text, bg=bg, fg=fg, command=command, width=width, height=height, **kwargs)
        self.config(font=("Arial", 12))
        self.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Add tooltip text when button is hovered over
        self.tooltip = None
        self.bind("<Enter>", self.show_tooltip)
        self.bind("<Leave>", self.hide_tooltip)

    def set_tooltip(self, text):
        self.tooltip = text

    def show_tooltip(self, event=None):
        if self.tooltip:
            x, y, cx, cy = self.bbox("insert")
            x += self.winfo_rootx() + 25
            y += self.winfo_rooty() + 20
            self.tooltip_window = tw = tk.Toplevel(self)
            tw.wm_overrideredirect(True)
            tw.wm_geometry("+%d+%d" % (x, y))
            label = tk.Label(tw, text=self.tooltip, justify='left', background="#ffffff", relief='solid', borderwidth=1,
                             font=("Arial", "10", "normal"))
            label.pack(ipadx=1)

    def hide_tooltip(self, event=None):
        if self.tooltip_window:
            self.tooltip_window.destroy()

    def set_text(self, text):
        self.config(text=text)

    def set_bg(self, bg):
        self.config(bg=bg)

    def set_fg(self, fg):
        self.config(fg=fg)

    def set_command(self, command):
        self.config(command=command)

    def set_width(self, width):
        self.config(width=width)

    def set_height(self, height):
        self.config(height=height)
