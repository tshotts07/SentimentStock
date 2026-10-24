import yfinance as yf

class DataFetcher:
  def __init__(self, ticker):
    self.ticker = ticker.upper()


  def get_stock_data(self):
    """Fetch last 5 days of stock closing prices"""
    try:
      stock = yf.Ticker(self.ticker)
      hist = stock.history(period="5d")
      if hist.empty:
        return None
      return hist['Close']
    except Exception as e:
      print(f"Error fetching data: {e}")
      return None

  def get_news_headlines(self):
    """
    MOCK DATA: In a production environment, this would be replaced with a call to an external API (Such as NewsAPI).
    Simulated for ease of demonstration and to avoid API key requirements.
    """
    return [
          f"{self.ticker} reports record-breaking quarterly earnings.",
          f"Analysts downgrade {self.ticker} citing supply chain concerns.",
          f"New product launch from {self.ticker} receives glowing reviews.",
          f"Market volatility impacts {self.ticker} stock price in early trading.",
          f"Investors remain optimistic about {self.ticker}'s long-term strategy."
      ]
