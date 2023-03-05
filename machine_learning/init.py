from .neural_network import NeuralNetwork
from .feature_engineering import FeatureEngineering
from .strategy_generation import StrategyGeneration
from .trading_simulation import TradingSimulation

class MachineLearning:
    def __init__(self):
        self.neural_network = NeuralNetwork()
        self.feature_engineering = FeatureEngineering()
        self.strategy_generation = StrategyGeneration()
        self.trading_simulation = TradingSimulation()

    def run_backtest(self, strategy, market_data):
        """
        Runs a backtest for a given strategy and market data.
        """
        signals = self.strategy_generation.generate_signals(strategy, market_data)
        portfolio = self.trading_simulation.run_simulation(signals, market_data)
        return portfolio

    def train_model(self, data):
        """
        Trains a neural network model with the given data.
        """
        X, y = self.feature_engineering.prepare_data(data)
        self.neural_network.train(X, y)

    def predict(self, data):
        """
        Makes predictions using the trained neural network model.
        """
        X = self.feature_engineering.prepare_data(data)
        return self.neural_network.predict(X)

    def evaluate_strategy(self, strategy, market_data):
        """
        Evaluates a strategy on the given market data.
        """
        signals = self.strategy_generation.generate_signals(strategy, market_data)
        results = self.trading_simulation.evaluate_strategy(signals, market_data)
        return results

    def optimize_strategy(self, strategy, market_data, optimization_function):
        """
        Optimizes a strategy on the given market data using the given optimization function.
        """
        signals = self.strategy_generation.generate_signals(strategy, market_data)
        optimized_strategy = optimization_function(signals, market_data)
        return optimized_strategy
