import matplotlib.pyplot as plt

class ScatterPlot:
    def __init__(self, title='', xlabel='', ylabel=''):
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

    def plot(self, x, y, color='blue', size=50, alpha=0.5, label=None):
        plt.scatter(x, y, c=color, s=size, alpha=alpha, label=label)
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.legend()
        plt.show()
