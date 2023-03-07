import time

class SleepTracker:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.total_sleep_time = None
        self.deep_sleep_time = None
        self.light_sleep_time = None
        self.rem_sleep_time = None
        self.quality_score = None
    
    def start_tracking(self):
        print("Starting sleep tracking...")
        self.start_time = time.time()
    
    def stop_tracking(self):
        print("Stopping sleep tracking...")
        self.end_time = time.time()
        self.total_sleep_time = self.end_time - self.start_time
        self.deep_sleep_time = self.get_deep_sleep_time()
        self.light_sleep_time = self.get_light_sleep_time()
        self.rem_sleep_time = self.get_rem_sleep_time()
        self.quality_score = self.get_quality_score()
        
    def get_deep_sleep_time(self):
        # Get deep sleep time from sleep data
        deep_sleep_time = 0
        
        # Calculate deep sleep time...
        
        return deep_sleep_time
    
    def get_light_sleep_time(self):
        # Get light sleep time from sleep data
        light_sleep_time = 0
        
        # Calculate light sleep time...
        
        return light_sleep_time
    
    def get_rem_sleep_time(self):
        # Get REM sleep time from sleep data
        rem_sleep_time = 0
        
        # Calculate REM sleep time...
        
        return rem_sleep_time
    
    def get_quality_score(self):
        # Get sleep quality score from sleep data
        quality_score = 0
        
        # Calculate sleep quality score...
        
        return quality_score
    
    def print_sleep_data(self):
        print("Sleep Data:")
        print(f"Total sleep time: {self.total_sleep_time} seconds")
        print(f"Deep sleep time: {self.deep_sleep_time} seconds")
        print(f"Light sleep time: {self.light_sleep_time} seconds")
        print(f"REM sleep time: {self.rem_sleep_time} seconds")
        print(f"Sleep quality score: {self.quality_score}")
