import datetime

class FitnessTracker:
    def __init__(self):
        self.workouts = []

    def add_workout(self, date, exercise, duration, calories_burned):
        """Add a new workout to the tracker"""
        workout = {
            'date': date,
            'exercise': exercise,
            'duration': duration,
            'calories_burned': calories_burned
        }
        self.workouts.append(workout)

    def get_workouts_by_date(self, date):
        """Get all workouts for a given date"""
        workouts_on_date = []
        for workout in self.workouts:
            if workout['date'] == date:
                workouts_on_date.append(workout)
        return workouts_on_date

    def get_total_calories_burned(self, start_date=None, end_date=None):
        """Get total calories burned for a given time period"""
        total_calories_burned = 0
        for workout in self.workouts:
            if start_date and datetime.datetime.strptime(workout['date'], '%Y-%m-%d').date() < start_date:
                continue
            if end_date and datetime.datetime.strptime(workout['date'], '%Y-%m-%d').date() > end_date:
                continue
            total_calories_burned += workout['calories_burned']
        return total_calories_burned

    def get_average_calories_burned(self, start_date=None, end_date=None):
        """Get average calories burned per workout for a given time period"""
        workouts = []
        for workout in self.workouts:
            if start_date and datetime.datetime.strptime(workout['date'], '%Y-%m-%d').date() < start_date:
                continue
            if end_date and datetime.datetime.strptime(workout['date'], '%Y-%m-%d').date() > end_date:
                continue
            workouts.append(workout)
        if len(workouts) == 0:
            return 0
        total_calories_burned = sum(workout['calories_burned'] for workout in workouts)
        return total_calories_burned / len(workouts)

    def get_most_common_exercises(self, start_date=None, end_date=None, num_exercises=3):
        """Get most common exercises for a given time period"""
        exercises = {}
        for workout in self.workouts:
            if start_date and datetime.datetime.strptime(workout['date'], '%Y-%m-%d').date() < start_date:
                continue
            if end_date and datetime.datetime.strptime(workout['date'], '%Y-%m-%d').date() > end_date:
                continue
            exercise = workout['exercise']
            if exercise in exercises:
                exercises[exercise] += 1
            else:
                exercises[exercise] = 1
        sorted_exercises = sorted(exercises.items(), key=lambda x: x[1], reverse=True)
        return [exercise[0] for exercise in sorted_exercises[:num_exercises]]

    def get_workouts_by_exercise(self, exercise):
        """Get all workouts for a given exercise"""
        workouts_for_exercise = []
        for workout in self.workouts:
            if workout['exercise'] == exercise:
                workouts_for_exercise.append(workout)
        return workouts_for_exercise
