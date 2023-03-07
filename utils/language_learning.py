import requests
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


class LanguageLearner:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.wordnet_lemmatizer = WordNetLemmatizer()
        
    def learn_word(self, word):
        """
        Given a word, retrieve its definition and examples from an online dictionary, 
        and return a dictionary containing the word, definition, and examples.
        """
        url = f"https://www.dictionary.com/browse/{word}"
        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')
        definition_section = soup.find('section', class_='css-1f12kn3 e1hk9ate4')

        definition = definition_section.find('span', class_='one-click-content css-nnyc96 e1q3nk1v1').get_text().strip()
        examples_section = definition_section.find('div', class_='luna-example')

        examples = []
        for example in examples_section.find_all('em'):
            examples.append(example.get_text().strip())

        return {"word": word, "definition": definition, "examples": examples}
    
    def learn_sentence(self, sentence):
        """
        Given a sentence, tokenize it, remove stop words, lemmatize words, and 
        return a list of words that are not stop words.
        """
        tokens = word_tokenize(sentence.lower())
        filtered_tokens = [token for token in tokens if not token in self.stop_words]
        lemmatized_tokens = [self.wordnet_lemmatizer.lemmatize(token) for token in filtered_tokens]
        return lemmatized_tokens
    
    def search_on_web(self, query):
        """
        Given a query, search for relevant information on the web using Google search, 
        and return a list of links to relevant webpages.
        """
        query = query.replace(" ", "+")
        url = f"https://www.google.com/search?q={query}"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
        page = requests.get(url, headers=headers)

        soup = BeautifulSoup(page.content, 'html.parser')
        links = []
        for link in soup.find_all("a", href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
            url = re.findall("(?<=/url\?q=)(htt.*://.*)", link['href'])[0]
            url = requests.utils.unquote(url)
            links.append(url)
        return links
