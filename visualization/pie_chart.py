import matplotlib.pyplot as plt


class PieChart:
    def __init__(self, title: str, labels: list, sizes: list):
        self.title = title
        self.labels = labels
        self.sizes = sizes

    def generate_chart(self):
        plt.pie(self.sizes, labels=self.labels, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')
        plt.title(self.title)
        plt.show()
