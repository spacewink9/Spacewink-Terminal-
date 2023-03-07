from utils.api import AlphaVantageAPI
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
from tensorflow.keras.optimizers import Adam
from datetime import datetime, timedelta


def get_stock_data(symbol: str, api_key: str) -> pd.DataFrame:
    """
    Helper function to get stock data using Alpha Vantage API
    """
    api = AlphaVantageAPI(api_key)
    data = api.get_stock_data(symbol=symbol)
    df = pd.DataFrame(data).transpose()
    df = df.astype(float)
    df = df.sort_index()
    return df


def preprocess_data(data: pd.DataFrame, window_size: int = 30) -> np.ndarray:
    """
    Function to preprocess the data for LSTM model
    """
    data = data.values
    scaler = MinMaxScaler()
    data = scaler.fit_transform(data)
    X = []
    y = []
    for i in range(window_size, len(data)):
        X.append(data[i-window_size:i, :])
        y.append(data[i, 0])
    X, y = np.array(X), np.array(y)
    return X, y, scaler


def build_lstm_model(input_shape: tuple) -> Sequential:
    """
    Function to build the LSTM model
    """
    model = Sequential()
    model.add(LSTM(units=128, input_shape=input_shape, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=64, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=32))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))
    model.compile(optimizer=Adam(learning_rate=0.001), loss="mean_squared_error")
    return model


def train_lstm_model(model: Sequential, X_train: np.ndarray, y_train: np.ndarray, epochs: int = 100) -> Sequential:
    """
    Function to train the LSTM model
    """
    model.fit(X_train, y_train, epochs=epochs, batch_size=32)
    return model


def make_prediction(model: Sequential, data: np.ndarray, scaler: MinMaxScaler, forecast_period: int) -> np.ndarray:
    """
    Function to make a prediction using the LSTM model
    """
    predictions = []
    last_window = data[-30:, :]
    last_window_scaled = scaler.transform(last_window)
    for i in range(forecast_period):
        next_day = model.predict(np.array([last_window_scaled]))
        predictions.append(next_day[0, 0])
        last_window = np.append(last_window, np.array([next_day]), axis=0)[1:, :]
        last_window_scaled = scaler.transform(last_window)
    predictions = np.array(predictions)
    return predictions, scaler.inverse_transform(predictions.reshape(-1, 1)).reshape(-1)


def run_auto_ai_analysis(api_key: str) -> None:
    """
    Function to run the Auto AI Analysis screen
    """
    print("Welcome to the Auto AI Analysis screen!")
    print("Please enter a stock symbol to get started.")
    symbol = input("> ").upper()
    print(f"Fetching data for {symbol}...")
    try:
        df = get_stock_data(symbol, api_key)
    except ValueError as e:
        print(e)
        return
    print("Data fetched successfully!")
    print("Please wait while we train our model...")
    X, y, scaler = preprocess_data(df)    X, y, scaler = preprocess_data(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    accuracy = model.score(X_test, y_test)
    print(f"Model accuracy: {accuracy*100:.2f}%")

    # Get the latest data for prediction
    latest_data = get_latest_data(symbol)

    # Preprocess the latest data
    latest_data = preprocess_latest_data(latest_data, scaler)

    # Make prediction
    prediction = model.predict(latest_data)

    # Print the prediction
    print("Prediction:")
    if prediction == 1:
        print("Buy")
    else:
        print("Sell")

with open("prediction.txt", "w") as file:
    file.write(str(prediction))

# Display a message to the user
print("Prediction saved to prediction.txt")

# Display a visualization of the prediction
plot_prediction(X_test, y_test, model)

# Ask the user if they want to save the model
save_model = input("Do you want to save the model? (y/n): ")
if save_model.lower() == "y":
    model.save("auto_ai_model.h5")
    print("Model saved successfully!")
else:
    print("Model not saved.")

# Ask the user if they want to run the analysis again
run_again = input("Do you want to run the analysis again? (y/n): ")
if run_again.lower() == "y":
    auto_ai_analysis()
else:
    print("Exiting auto AI analysis screen.")
