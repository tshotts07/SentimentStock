import sys
from data_fetcher import DataFetcher
from analyzer import SentimentAnalyzer

def main():
  print("\n" + "="*40)
  print("    Sentiment Stock Analyzer    ")
  print("="*40)

  # Get User input
  symbol = input("\nEnter Stock Ticker (e.g. AAPL, TSLA, MSFT): ").strip().upper()

  if not symbol:
    print(" Error: No ticker symbol provided.")
    return


  # Initialize modules
  fetcher = DataFetcher(symbol)
  analyzer = SentimentAnalyzer()


  # Get Price Data
  print(f"\n[1/3] Fetching market data for {symbol}...")
  prices = fetcher.get_stock_data()

  if prices is None or len(prices) < 2:
    print(f" Error: Could not retrieve data for '{symbol}'. Please check the symbol and your internet connection.")
    return

  # Get and Analyze News Sentiment
  print(f"[2/3] Analyzing recent news sentiment...")
  headlines = fetcher.get_news_headlines()
  score = analyzer.get_sentiment_score(headlines)
  sentiment_label = analyzer.interpret_score(score)

  # Calculate Performance & Display Report
  current_price = prices.iloc[-1]
  starting_price = prices.iloc[0]
  price_change = ((current_price - starting_price) / starting_price) * 100

  print(f"[3/3] Analysis Complete.\n")
  print(f"--- FINAL REPORT: {symbol} ---")
  print(f"Current Price:     ${current_price:.2f}")
  print(f"5-Day Price Trend: {price_change:+.2f}%")
  print(f"Sentiment Score:   {score:.2f} (-1.0 to 1.0)")
  print(f"Market Mood:       {sentiment_label}")
  print("-" * 30)
  print("Disclaimer: This is a demo tool. Do not use for actual trading decisions.\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting application...")
        sys.exit()
    except Exception as e:
        print(f"\n[!] An unexpected error occurred: {e}")
