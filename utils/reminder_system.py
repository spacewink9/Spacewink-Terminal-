import datetime
import time

class Reminder:
    def __init__(self):
        self.reminders = []

    def add_reminder(self, reminder, date_time):
        self.reminders.append((reminder, date_time))

    def check_reminders(self):
        while True:
            now = datetime.datetime.now()
            for reminder in self.reminders:
                if now >= reminder[1]:
                    print(f"Reminder: {reminder[0]}")
                    self.reminders.remove(reminder)
            time.sleep(1)
