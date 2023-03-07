import random
import time
import speech_recognition as sr

class VoiceActivatedGames:
    def __init__(self):
        self.r = sr.Recognizer()
        self.games = {
            "guessing game": self.guessing_game,
            "rock paper scissors": self.rock_paper_scissors,
            "dice game": self.dice_game
        }
    
    def start_game(self):
        with sr.Microphone() as source:
            print("Say the name of the game you want to play")
            audio = self.r.listen(source)
            
            try:
                text = self.r.recognize_google(audio)
                print("You said: ", text)
                game = self.games.get(text.lower())
                if game:
                    game()
                else:
                    print("Sorry, I didn't recognize that game. Please try again.")
                    self.start_game()
            except sr.UnknownValueError:
                print("Sorry, I didn't catch that. Please try again.")
                self.start_game()
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    def guessing_game(self):
        print("Welcome to the guessing game!")
        number = random.randint(1, 100)
        guesses = 0
        
        while True:
            with sr.Microphone() as source:
                print("Guess a number between 1 and 100")
                audio = self.r.listen(source)
                
                try:
                    guess = int(self.r.recognize_google(audio))
                    print("You guessed: ", guess)
                    guesses += 1
                    
                    if guess == number:
                        print("Congratulations! You guessed the number in", guesses, "guesses!")
                        break
                    elif guess < number:
                        print("Too low. Guess again!")
                    else:
                        print("Too high. Guess again!")
                
                except sr.UnknownValueError:
                    print("Sorry, I didn't catch that. Please try again.")
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    def rock_paper_scissors(self):
        print("Let's play rock, paper, scissors!")
        
        while True:
            with sr.Microphone() as source:
                print("Choose rock, paper, or scissors")
                audio = self.r.listen(source)
                
                try:
                    choice = self.r.recognize_google(audio)
                    print("You chose: ", choice)
                    computer_choice = random.choice(["rock", "paper", "scissors"])
                    print("Computer chose: ", computer_choice)
                    
                    if choice == computer_choice:
                        print("It's a tie!")
                    elif (choice == "rock" and computer_choice == "scissors") or \
                        (choice == "paper" and computer_choice == "rock") or \
                        (choice == "scissors" and computer_choice == "paper"):
                        print("You win!")
                        break
                    else:
                        print("You lose. Try again!")
                
                except sr.UnknownValueError:
                    print("Sorry, I didn't catch that. Please try again.")
                except sr.RequestError as e:
                    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    def dice_game(self):
        print("Let's play the dice game!")
        total_score = 0
        
        while True:
            with sr.Microphone() as source:
                print("Press any key to roll the dice")
                audio = self.r.listen(source)
                print("
