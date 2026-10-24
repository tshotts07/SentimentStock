# SentimentStock

SentimentStock is a Python-based financial analysis tool that correlates market news sentiment with recent stock price performance. It demonstrates the use of Natural Language Processing (NLP) to quantify market mood and helps users visualize how news might impact stock trends.

## Features
- **Real-time Price Data:** Fetches the latest market prices using the `yfinance` API.
- **NLP Sentiment Analysis:** Utilizes `TextBlob` to analyze news headlines and generate a polarity score.
- **Trend Calculation:** Automatically calculates 5-day price changes to provide context to the sentiment.
- **Modular Architecture:** Clean, object-oriented Python code that is easy to scale and maintain.

## Built With
- [Python](https://www.python.org/) - Core logic
- [yfinance](https://github.com/ranaroussi/yfinance) - Financial data source
- [TextBlob](https://textblob.readthedocs.io/) - Sentiment processing
- [Pandas](https://pandas.pydata.org/) - Data manipulation

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/SentimentStock.git
   cd SentimentStock
