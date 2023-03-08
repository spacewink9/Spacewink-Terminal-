import matplotlib.pyplot as plt
from typing import List, Tuple

def generate_line_chart(x_values: List[float], y_values: List[float], title: str, x_label: str, y_label: str, 
                         line_color: str = 'blue') -> None:
    """Generates a line chart using Matplotlib with the given data and settings."""
    
    plt.plot(x_values, y_values, color=line_color)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
    
def generate_multiple_line_charts(data: List[Tuple[List[float], List[float], str, str, str, str]]) -> None:
    """Generates multiple line charts using Matplotlib with the given data and settings."""
    
    num_charts = len(data)
    
    fig, axs = plt.subplots(nrows=num_charts, figsize=(10, 8 * num_charts))
    
    for i, (x_values, y_values, title, x_label, y_label, line_color) in enumerate(data):
        axs[i].plot(x_values, y_values, color=line_color)
        axs[i].set_title(title)
        axs[i].set_xlabel(x_label)
        axs[i].set_ylabel(y_label)
    
    plt.tight_layout()
    plt.show()
