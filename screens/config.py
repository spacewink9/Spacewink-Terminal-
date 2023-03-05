class AdvancedSettings:
    def __init__(self):
        self.enable_technical_indicators = True
        self.enable_fundamental_analysis = False
        self.enable_sentiment_analysis = False
        self.enable_machine_learning = False
        self.enable_portfolio_optimization = False
        self.enable_risk_analysis = False

    def set_technical_indicators(self, value):
        self.enable_technical_indicators = value

    def set_fundamental_analysis(self, value):
        self.enable_fundamental_analysis = value

    def set_sentiment_analysis(self, value):
        self.enable_sentiment_analysis = value

    def set_machine_learning(self, value):
        self.enable_machine_learning = value

    def set_portfolio_optimization(self, value):
        self.enable_portfolio_optimization = value

    def set_risk_analysis(self, value):
        self.enable_risk_analysis = value
