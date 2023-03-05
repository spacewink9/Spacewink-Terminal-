class Feed:
    def __init__(self):
        self.bars = []

    def add_bar(self, bar):
        self.bars.append(bar)

    def get_latest_bar(self):
        if len(self.bars) > 0:
            return self.bars[-1]
        else:
            return None

    def get_latest_bars(self, n=1):
        if len(self.bars) > 0:
            return self.bars[-n:]
        else:
            return None

    def get_all_bars(self):
        return self.bars

    def get_latest_bar_datetime(self):
        latest_bar = self.get_latest_bar()
        if latest_bar is not None:
            return latest_bar.timestamp
        else:
            return None
