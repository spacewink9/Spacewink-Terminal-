import random

class MeditationAndMindfulness:
    
    def __init__(self):
        self.meditation_techniques = ['Mindful Breathing', 'Body Scan Meditation', 'Loving-Kindness Meditation']
        self.mindfulness_techniques = ['Gratitude Journaling', 'Visualizations', 'Yoga']
        
    def get_personalized_exercise(self, preference):
        if preference == 'stress':
            exercise = random.choice(self.mindfulness_techniques)
        elif preference == 'anxiety':
            exercise = random.choice(self.meditation_techniques)
        else:
            exercise = random.choice(self.meditation_techniques + self.mindfulness_techniques)
        return exercise
    
    def start_meditation(self, technique):
        print(f"Starting {technique}...")
        # Code to initiate the meditation or mindfulness exercise
        print("Meditation complete.")
