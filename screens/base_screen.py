class BaseScreen:
    def __init__(self, name):
        self.name = name

    def display(self):
        raise NotImplementedError("Subclasses must implement display() method")
