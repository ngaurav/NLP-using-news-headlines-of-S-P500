from google.cloud import language
import math

def analyzeText(text):
    print ("Performing sentiment analysis.")

    #API_SIZE_LIMIT = 1000000
    #text = text[:API_SIZE_LIMIT]
    language_client = language.Client()
    pos = 0
    neg = 0
    for news in text.split('~'):
        document = language_client.document_from_text(news)
        sentiment = document.analyze_sentiment().sentiment
        pos += math.exp(sentiment.score)*sentiment.magnitude
        neg += math.exp(-sentiment.score)*sentiment.magnitude

    return pos, neg
