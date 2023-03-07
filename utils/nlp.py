import spacy
from spacy.matcher import PhraseMatcher

class NLP:

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.matcher = PhraseMatcher(self.nlp.vocab)
        self.reminders = []
        self.events = []

    def extract_entities(self, text):
        doc = self.nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities

    def add_event(self, event):
        self.events.append(event)

    def add_reminder(self, reminder):
        self.reminders.append(reminder)

    def search_events(self, keyword):
        results = []
        for event in self.events:
            if keyword.lower() in event.lower():
                results.append(event)
        return results

    def search_reminders(self, keyword):
        results = []
        for reminder in self.reminders:
            if keyword.lower() in reminder.lower():
                results.append(reminder)
        return results

    def add_phrase_matcher(self, phrases):
        patterns = [self.nlp(text) for text in phrases]
        self.matcher.add("MatchPhrases", None, *patterns)

    def find_matches(self, text):
        doc = self.nlp(text)
        matches = self.matcher(doc)
        results = []
        for match_id, start, end in matches:
            matched_span = doc[start:end]
            results.append(matched_span.text)
        return results

    def summarize_text(self, text):
        doc = self.nlp(text)
        summary = []
        for sent in doc.sents:
            summary.append(sent.text)
            if len(summary) >= 3:
                break
        return " ".join(summary)
      )
      def generate_keywords(text):
    """
    Generates keywords from given text using NLP techniques.

    Args:
    text (str): The text to generate keywords from.

    Returns:
    List[str]: A list of keywords generated from the text.
    """
    # Instantiate the TextBlob object
    blob = TextBlob(text)

    # Generate keywords using the TextBlob noun phrase extraction method
    keywords = []
    for phrase in blob.noun_phrases:
        # Remove any stop words from the phrase
        words = [word for word in phrase.split() if word not in stopwords.words('english')]
        # Add the remaining words to the keywords list
        keywords += words

    # Remove any duplicate keywords
    keywords = list(set(keywords))

    # Return the keywords
    return keywords

