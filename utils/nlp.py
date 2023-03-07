import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest
from textblob import TextBlob

nlp = spacy.load('en_core_web_sm')

def text_sentiment(text):
    """
    Get the sentiment of the given text using TextBlob library.

    Args:
    text (str): The input text.

    Returns:
    str: The sentiment of the text ('positive', 'neutral', or 'negative').
    """
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return 'positive'
    elif sentiment == 0:
        return 'neutral'
    else:
        return 'negative'

def text_summary(text):
    """
    Get a summary of the given text by selecting the most important sentences.

    Args:
    text (str): The input text.

    Returns:
    str: The summary of the text.
    """
    doc = nlp(text)
    sentences = [sent for sent in doc.sents]

    word_frequencies = Counter()
    for word in doc:
        if word.text.lower() not in STOP_WORDS:
            word_frequencies[word.text.lower()] += 1

    maximum_frequency = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequency)

    sentence_scores = {}
    for sent in sentences:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if len(sent.text.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]

    summary_sentences = nlargest(3, sentence_scores, key=sentence_scores.get)
    summary = [sent.text for sent in summary_sentences]
    return " ".join(summary)

def text_keywords(text):
    """
    Get the most important keywords from the given text.

    Args:
    text (str): The input text.

    Returns:
    list: The most important keywords from the text.
    """
    doc = nlp(text)
    tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]
    word_frequencies = Counter(tokens)

    # Get the top 5 most common keywords
    common_words = word_frequencies.most_common(5)

    # Remove any duplicate keywords
    keywords = list(set([word[0] for word in common_words]))

    # Return the keywords
    return keywords
