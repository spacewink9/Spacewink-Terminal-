import matplotlib.pyplot as plt


def plot_candlestick_chart(df):
    """
    Plot a candlestick chart using the data from a pandas dataframe.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe containing the OHLC data.
    """

    # Set up the figure and axes
    fig, ax = plt.subplots()

    # Plot the candlestick chart
    candlestick_ohlc(ax, df.values, width=0.6, colorup='green', colordown='red')

    # Set the x-axis label and format the date
    ax.set_xlabel('Date')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    # Set the y-axis label and format the prices
    ax.set_ylabel('Price')
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

    # Rotate the x-axis labels for better visibility
    plt.xticks(rotation=45)

    # Show the plot
    plt.show()


def plot_line_chart(df, x_col, y_col):
    """
    Plot a line chart using the data from a pandas dataframe.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe containing the data to plot.
    x_col : str
        The column name to use for the x-axis data.
    y_col : str
        The column name to use for the y-axis data.
    """

    # Set up the figure and axes
    fig, ax = plt.subplots()

    # Plot the line chart
    ax.plot(df[x_col], df[y_col])

    # Set the x-axis label and format the date
    ax.set_xlabel('Date')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    # Set the y-axis label and format the prices
    ax.set_ylabel('Price')
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

    # Rotate the x-axis labels for better visibility
    plt.xticks(rotation=45)

    # Show the plot
    plt.show()


# Add more visualization functions here as needed
