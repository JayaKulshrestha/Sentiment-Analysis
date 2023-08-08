from textblob import TextBlob


def analyze_sentiment(text):
    # Create a textblob object
    blob =TextBlob(text)
    
    # Perform sentiment analysis
    sentiment = blob.sentiment.polarity
    
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"
    
input_text =input("Enter the sentence for sentiment analysis:\n")

#Analyze Sentiment

sentiment_result = analyze_sentiment(input_text)

print("Sentiment:",sentiment_result)