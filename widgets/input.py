import tkinter as tk

class Input(tk.Frame):
    def __init__(self, master, label_text, default_value='', **kwargs):
        super().__init__(master, **kwargs)
        
        self.label_text = label_text
        self.default_value = default_value
        
        self.label = tk.Label(self, text=self.label_text)
        self.label.pack(side='left', padx=5)
        
        self.entry = tk.Entry(self)
        self.entry.insert(0, self.default_value)
        self.entry.pack(side='left', padx=5)
    
    def get(self):
        return self.entry.get()
    
    def set(self, value):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)
