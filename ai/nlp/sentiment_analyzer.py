from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0.5:
        return 'positive'
    elif polarity < -0.5:
        return 'very negative'
    elif polarity < 0:
        return 'negative'
    else:
        return 'neutral'


