import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Define function to speak a string
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Define function to greet the user
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am your virtual assistant. How may I assist you?")


# Define function to listen to microphone input and return as string
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print("Sorry, I could not understand. Please say that again.")
        query = None

    return query


# Define function to send email
def send_email(to, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your_email@gmail.com', 'your_password')
    server.sendmail('your_email@gmail.com', to, f"Subject: {subject}\n\n{message}")
    server.quit()


# Define main function to handle user requests
def main():
    greet()

    while True:
        query = listen()

        # Some advanced features and functionality
        if query:

            # Open a website
            if 'open' in query.lower() and 'website' in query.lower():
                speak("Which website should I open?")
                website = listen().lower()
                if website:
                    webbrowser.open(f"https://www.{website}.com")

            # Search something on Google
            elif 'search' in query.lower() and 'google' in query.lower():
                speak("What should I search for?")
                search_term = listen().lower()
                if search_term:
                    webbrowser.open(f"https://www.google.com/search?q={search_term}")

            # Get current time
            elif 'time' in query.lower():
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                speak(f"The time is {current_time}")

            # Get today's date
            elif 'date' in query.lower():
                today = datetime.date.today().strftime("%B %d, %Y")
                speak(f"Today's date is {today}")

            # Send an email
            elif 'send email' in query.lower():
                speak("To whom should I send the email?")
                to = input().lower()
                speak("What should be the subject of the email?")
                subject = listen().capitalize()
                speak("What message should I send?")
                message = listen().capitalize()
                send_email(to, subject, message)
                speak("The email has been sent.")

                    # Get information from Wikipedia
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # Open YouTube
        elif 'open youtube' in query:
            speak('Opening YouTube...')
            webbrowser.open("youtube.com")

        # Open Google
        elif 'open google' in query:
            speak('Opening Google...')
            webbrowser.open("google.com")

        # Open Gmail
        elif 'open gmail' in query:
            speak('Opening Gmail...')
            webbrowser.open("gmail.com")

        # Get current date and time
        elif 'what time is it' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'what is the date' in query:
            today = date.today()
            d = today.strftime("%B %d, %Y")
            speak(f"Today's date is {d}")

        # Play music
        elif 'play music' in query:
            music_dir = 'C:/Users/Public/Music/Sample Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        # Tell a joke
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        # Take a screenshot
        elif 'take a screenshot' in query:
            screenshot = pyautogui.screenshot()
            screenshot.save("screenshot.png")
            speak("Screenshot taken and saved!")

        # Open code editor
        elif 'open code editor' in query:
            speak('Opening Visual Studio Code...')
            os.startfile("C:\\Users\\Username\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        # Send an email
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "recipient_email_address@example.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I was not able to send the email at this time.")

        # Exit the program
        elif 'exit' in query:
            speak("Goodbye!")
            exit()
