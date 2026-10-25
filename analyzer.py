from textblob import TextBlob

class SentimentAnalyzer:
  @staticmethod
  def get_sentiment_score(headlines):
    """
    Calculates avg. polarity score: -1 (Negative) to 1 (Positive).
    Uses TextBlob's pre-trained NLP model.
    """
    if not headlines:
      return 0

    # Calculates polarity (how positive or negative the text is)
    scores = [TextBlob(h).sentiment.polarity for h in headlines]
    return sum(scores) / len(scores)

  @staticmethod
  def interpret_score(score):
    """Categorizes score into readable format."""
    if score > 0.1:
      return "Bullish (Positive Sentiment)
    elif score < -0.1:
      return "Bearish (Negative Sentiment)
    else:
      return "Neutral"
