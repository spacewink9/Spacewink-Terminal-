import speech_recognition as sr
import webbrowser
import os
import re
import nltk
from nltk.corpus import stopwords

# Define stop words for NLP processing
stop_words = set(stopwords.words('english'))

# Function to perform voice search
def voice_search():
    # Initialize speech recognizer
    r = sr.Recognizer()
    
    # Set microphone as audio source
    with sr.Microphone() as source:
        print("Speak your search query...")
        audio = r.listen(source)
    
    try:
        # Use Google Speech Recognition to transcribe audio
        query = r.recognize_google(audio)
        print("You said: " + query)
        
        # Remove stop words and special characters for NLP processing
        query = re.sub('[^A-Za-z0-9\s]+', '', query)
        query = " ".join([word for word in query.split() if word.lower() not in stop_words])
        
        # Perform web search using processed query
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
    except sr.UnknownValueError:
        print("Sorry, your search query could not be recognized.")
    except sr.RequestError:
        print("Could not connect to Google Speech Recognition service.")
