import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text
    except:
        return None
from utils.voice_text import speak, listen

speak("Welcome to the Spacewink Terminal. How can I help you today?")
text = listen()
if text is not None:
    print(f"User said: {text}")
else:
    print("Sorry, I didn't catch that. Can you please repeat?")
