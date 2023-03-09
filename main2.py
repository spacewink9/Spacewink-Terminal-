import tkinter as tk
from widgets import Button, Label, Dropdown, Input, Table
from exchanges import AlphaVantage, Binance, Bitfinex, Bitstamp

# Create the main application window
root = tk.Tk()
root.title("Spacewink Terminal")
root.geometry("800x600")

# Create a label widget to display the title
title_label = Label(root, text="Spacewink Terminal", font=("Arial", 24))
title_label.pack()

# Create a dropdown widget to select the exchange
exchange_label = Label(root, text="Select Exchange:")
exchange_label.pack(side=tk.LEFT)
exchange_options = ["AlphaVantage", "Binance", "Bitfinex", "Bitstamp"]
exchange_dropdown = Dropdown(root, options=exchange_options)
exchange_dropdown.pack(side=tk.LEFT)

# Create input widgets to enter API key and secret
api_key_label = Label(root, text="API Key:")
api_key_label.pack()
api_key_input = Input(root)
api_key_input.pack()

secret_label = Label(root, text="Secret:")
secret_label.pack()
secret_input = Input(root)
secret_input.pack()

# Create a button to fetch data from the selected exchange
fetch_button = Button(root, text="Fetch Data")
fetch_button.pack()

# Create a table to display the fetched data
table_columns = ["Date", "Open", "High", "Low", "Close", "Volume"]
table_data = []
table = Table(root, columns=table_columns, data=table_data)
table.pack()

# Define a function to fetch data from the selected exchange
def fetch_data():
    # Get the selected exchange and its API key and secret
    selected_exchange = exchange_dropdown.get_value()
    api_key = api_key_input.get_value()
    secret = secret_input.get_value()
    
    # Call the appropriate API to fetch data
    if selected_exchange == "AlphaVantage":
        exchange = AlphaVantage(api_key)
    elif selected_exchange == "Binance":
        exchange = Binance(api_key, secret)
    elif selected_exchange == "Bitfinex":
        exchange = Bitfinex(api_key, secret)
    elif selected_exchange == "Bitstamp":
        exchange = Bitstamp(api_key, secret)
    
    # Fetch the data and update the table
    data = exchange.fetch_data()
    table.set_data(data)

# Bind the fetch button to the fetch_data() function
fetch_button.bind("<Button-1>", lambda event: fetch_data())

# Start the main event loop
root.mainloop()
