import matplotlib.pyplot as plt

class VolumeChart:
    def __init__(self, data, symbol):
        self.data = data
        self.symbol = symbol
    
    def plot(self):
        fig, ax = plt.subplots(figsize=(12,8))

        # Create volume bars
        ax.bar(self.data.index, self.data['Volume'], color='gray', alpha=0.4)

        # Set title and axis labels
        ax.set_title(f'{self.symbol} Volume Chart')
        ax.set_xlabel('Date')
        ax.set_ylabel('Volume')

        # Set x-axis tick labels to appear only on Mondays
        ax.xaxis.set_major_locator(plt.MaxNLocator(10))

        # Set grid lines
        ax.grid(True)

        # Show plot
        plt.show()
