import requests

class TranslationService:
    
    # Supported languages
    SUPPORTED_LANGUAGES = {'en': 'English', 'hi': 'Hindi'}
    
    # API endpoint
    API_ENDPOINT = 'https://api-free.deepl.com/v2/translate'
    
    # API key
    API_KEY = '<YOUR_API_KEY>' # replace with your own API key
    
    def __init__(self, lang='en'):
        self.lang = lang
        
    def set_language(self, lang):
        if lang in self.SUPPORTED_LANGUAGES:
            self.lang = lang
            print(f"Language set to {self.SUPPORTED_LANGUAGES[lang]}")
        else:
            print("Invalid language code.")
            
    def translate(self, text, target_lang=None):
        if target_lang is None:
            target_lang = 'en' if self.lang == 'hi' else 'hi'
        if target_lang not in self.SUPPORTED_LANGUAGES:
            print("Invalid target language code.")
            return
        data = {
            'auth_key': self.API_KEY,
            'text': text,
            'target_lang': target_lang
        }
        response = requests.post(self.API_ENDPOINT, data=data)
        if response.status_code == 200:
            return response.json()['translations'][0]['text']
        else:
            print("Error in translation.")
            return None
