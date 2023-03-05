import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

class StrategyGenerator:
    def __init__(self, data, target_col):
        self.data = data
        self.target_col = target_col
        self.model = None

    def preprocess_data(self):
        # Perform data preprocessing steps such as imputation, scaling, feature engineering, etc.
        # For example, we can fill missing values with 0 and drop any rows with missing values
        self.data.fillna(0, inplace=True)
        self.data.dropna(inplace=True)

    def train_model(self):
        # Split data into training and testing sets
        X = self.data.drop(columns=[self.target_col])
        y = self.data[self.target_col]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train a random forest classifier
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)

        # Evaluate the model on the testing set
        score = self.model.score(X_test, y_test)
        print(f"Model accuracy: {score:.2f}")

    def generate_strategy(self, market_data):
        # Use the trained model to generate a buy/sell signal based on the market data
        # For example, we can calculate the RSI and MACD indicators and use them as features for the model
        rsi = market_data["rsi"]
        macd = market_data["macd"]
        features = pd.DataFrame({"rsi": rsi, "macd": macd})

        # Make a prediction using the trained model
        signal = self.model.predict(features)

        # Convert the signal to a buy/sell recommendation
        if signal == 1:
            recommendation = "buy"
        else:
            recommendation = "sell"

        return recommendation
