import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from typing import List
from strategy.base_strategy import BaseStrategy


class MachineLearningStrategy(BaseStrategy):

    def __init__(self, config: dict, name: str):
        super().__init__(config, name)
        self.model = None

    def set_config(self, config: dict):
        super().set_config(config)
        # Additional config parameters for machine learning strategy
        self.features = config.get('features', [])
        self.label = config.get('label', '')

    def train_model(self, X: pd.DataFrame, y: pd.Series):
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train a Random Forest classifier
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)

        # Print the accuracy score
        print(f'Training accuracy: {self.model.score(X_train, y_train)}')
        print(f'Testing accuracy: {self.model.score(X_test, y_test)}')

    def compute_signals(self, prices: pd.DataFrame) -> pd.DataFrame:
        # Prepare the input data for the machine learning model
        X = prices[self.features].values
        y = prices[self.label].values

        # Train the machine learning model
        self.train_model(X, y)

        # Use the model to generate signals
        predicted_labels = self.model.predict(X)
        signals = pd.Series(data=predicted_labels, index=prices.index, name='signal')

        return signals
