from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import math

def analyzeText(text):
    print ("Performing sentiment analysis.")

    #API_SIZE_LIMIT = 1000000
    #text = text[:API_SIZE_LIMIT]
    language_client = language.LanguageServiceClient()
    pos = 0
    neg = 0
    for news in text.split('~'):
        document = types.Document(content=news, type=enums.Document.Type.PLAIN_TEXT)
        sentiment = language_client.analyze_sentiment(document).document_sentiment
        pos += math.exp(sentiment.score)*sentiment.magnitude
        neg += math.exp(-sentiment.score)*sentiment.magnitude

    return pos, neg
