import plotly.graph_objs as go

def plot_candlestick(df):
    """Plots candlestick chart for a given dataframe."""
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                                         open=df['Open'],
                                         high=df['High'],
                                         low=df['Low'],
                                         close=df['Close'])])
    fig.show()
