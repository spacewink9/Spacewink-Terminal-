from screens.base_screen import BaseScreen
from market_data.market_data import MarketData
from machine_learning.feature_engineering import FeatureEngineering
from machine_learning.portfolio_optimization import PortfolioOptimization

class PortfolioOptimizationScreen(BaseScreen):
    def __init__(self, terminal):
        super().__init__(terminal)
        self.market_data = MarketData()
        self.feature_engineering = FeatureEngineering()
        self.portfolio_optimization = PortfolioOptimization()

    def display(self):
        self.clear_screen()
        print("=== Portfolio Optimization Screen ===")
        symbols_str = self.get_user_input("Enter comma-separated list of symbols to optimize portfolio for: ")
        symbols = [symbol.strip() for symbol in symbols_str.split(",")]

        # Get market data for symbols
        bars_by_symbol = {}
        for symbol in symbols:
            bars_by_symbol[symbol] = self.market_data.get_latest_bars(symbol, 100)

        # Feature engineering
        X, y, feature_names = self.feature_engineering.create_features_from_bars(bars_by_symbol)

        # Portfolio optimization
        weights = self.portfolio_optimization.optimize_portfolio(X, y)

        # Display results
        print(f"\nOptimal portfolio weights for symbols: {symbols}")
        for i in range(len(weights)):
            print(f"{symbols[i]}: {weights[i]}")

        print("\nFeature importances:")
        for i in range(len(feature_names)):
            print(f"{feature_names[i]}: {self.portfolio_optimization.feature_importances[i]}")
