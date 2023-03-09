import time

class ProgressBar:
    def __init__(self, length=20):
        self.length = length
        self.progress = 0
    
    def update(self, progress):
        self.progress = progress
    
    def display(self):
        filled_length = int(self.length * self.progress)
        bar = '=' * filled_length + '-' * (self.length - filled_length)
        print(f'|{bar}| {self.progress*100:.1f}%')
        

if __name__ == '__main__':
    bar = ProgressBar()
    for i in range(101):
        bar.update(i/100)
        bar.display()
        time.sleep(0.1)
