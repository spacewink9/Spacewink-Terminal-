from datetime import datetime
import os
import pandas as pd


class DataStorage:
    """
    Class for storing and retrieving data.
    """
    def __init__(self, data_folder):
        """
        Initializes the data storage object.
        
        Parameters
        ----------
        data_folder : str
            The path to the data folder.
        """
        self.data_folder = data_folder
    
    def save_data(self, data, filename):
        """
        Saves data to a file.
        
        Parameters
        ----------
        data : pd.DataFrame
            The data to save.
        filename : str
            The name of the file to save to.
        """
        filepath = os.path.join(self.data_folder, filename)
        data.to_csv(filepath, index=False)
    
    def load_data(self, filename):
        """
        Loads data from a file.
        
        Parameters
        ----------
        filename : str
            The name of the file to load from.
            
        Returns
        -------
        pd.DataFrame
            The loaded data.
        """
        filepath = os.path.join(self.data_folder, filename)
        return pd.read_csv(filepath)
    
    def save_trade(self, trade, filename):
        """
        Saves a trade to a file.
        
        Parameters
        ----------
        trade : dict
            A dictionary containing the trade data.
        filename : str
            The name of the file to save to.
        """
        filepath = os.path.join(self.data_folder, filename)
        with open(filepath, 'a') as f:
            f.write(f"{datetime.now()} {trade}\n")
    
    def load_trades(self, filename):
        """
        Loads trades from a file.
        
        Parameters
        ----------
        filename : str
            The name of the file to load from.
            
        Returns
        -------
        list
            A list of trades in the format of dictionaries.
        """
        filepath = os.path.join(self.data_folder, filename)
        with open(filepath, 'r') as f:
            trades = []
            for line in f:
                timestamp, trade = line.strip().split(' ', 1)
                trade = eval(trade)
                trades.append(trade)
        return trades
