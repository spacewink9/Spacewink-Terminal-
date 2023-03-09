import curses

class TextBox:
    def __init__(self, window, x, y, width, height, prompt):
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.prompt = prompt
        self.input = ""

    def draw(self):
        self.window.addstr(self.y, self.x, self.prompt, curses.color_pair(3))
        self.window.addstr(self.y + 1, self.x + 1, self.input)
        self.window.refresh()

    def handle_input(self, key):
        if key == curses.KEY_BACKSPACE or key == 127:
            self.input = self.input[:-1]
        elif key == ord('\n'):
            self.clear()
        else:
            self.input += chr(key)

    def clear(self):
        self.input = ""

    def get_text(self):
        return self.input
