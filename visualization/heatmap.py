import numpy as np
import matplotlib.pyplot as plt

class Heatmap:
    def __init__(self, data, row_labels, col_labels, title):
        """
        Initialize the Heatmap object.

        :param data: a 2D numpy array containing the data to be plotted
        :param row_labels: a list of labels for the rows
        :param col_labels: a list of labels for the columns
        :param title: a string containing the title of the heatmap
        """
        self.data = data
        self.row_labels = row_labels
        self.col_labels = col_labels
        self.title = title

    def plot(self):
        """
        Plot the heatmap.
        """
        fig, ax = plt.subplots()
        im = ax.imshow(self.data)

        # Set the tick labels
        ax.set_xticks(np.arange(len(self.col_labels)))
        ax.set_yticks(np.arange(len(self.row_labels)))
        ax.set_xticklabels(self.col_labels)
        ax.set_yticklabels(self.row_labels)

        # Rotate the tick labels and set their alignment
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

        # Set the title and colorbar
        ax.set_title(self.title)
        fig.tight_layout()
        plt.colorbar(im)

        # Show the plot
        plt.show()
