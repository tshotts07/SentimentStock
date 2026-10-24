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
    pass
