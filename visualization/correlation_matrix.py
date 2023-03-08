import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation_matrix(data: pd.DataFrame) -> None:
    """
    Plots the correlation matrix for the given data.
    """
    # Calculate the correlation matrix
    corr_matrix = data.corr()

    # Set up the plot
    plt.figure(figsize=(10, 10))
    plt.title('Correlation Matrix')

    # Plot the heatmap using Seaborn
    sns.heatmap(corr_matrix, vmin=-1, vmax=1, center=0, cmap='coolwarm',
                square=True, annot=True, fmt='.2f')

    # Show the plot
    plt.show()
