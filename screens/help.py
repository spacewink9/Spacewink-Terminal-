class Analysis:
    def __init__(self):
        self.exchange = None
        self.market = None
        self.interval = None
        self.indicators = []

    def set_exchange(self, exchange):
        self.exchange = exchange
        print(f"Exchange set to: {exchange}")

    def set_market(self, market):
        self.market = market
        print(f"Market set to: {market}")

    def set_interval(self, interval):
        self.interval = interval
        print(f"Interval set to: {interval}")

    def add_indicator(self, indicator):
        self.indicators.append(indicator)
        print(f"Indicator added: {indicator}")

    def remove_indicator(self, indicator):
        if indicator in self.indicators:
            self.indicators.remove(indicator)
            print(f"Indicator removed: {indicator}")
        else:
            print(f"Indicator {indicator} not found")

    def print_settings(self):
        print(f"Exchange: {self.exchange}")
        print(f"Market: {self.market}")
        print(f"Interval: {self.interval}")
        print(f"Indicators: {self.indicators}")
