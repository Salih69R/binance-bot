# main.py

from binance.client import Client
from strategy.ITradingStrategy import ITradingStrategy
from strategy.MyTradingStrategy import MyTradingStrategy 
from portfolio.MyPortfolio import MyPortfolio
from trader.MyTrader import MyTrader

def main(api_key: str, api_secret: str) -> None:
    # Initialize the Binance client
    client = Client(api_key, api_secret)

    # Create instances of your trading strategy and portfolio
    strategy: ITradingStrategy = MyTradingStrategy()
    portfolio = MyPortfolio(client)

    # Create an instance of the trader and inject dependencies
    trader = MyTrader(client, strategy, portfolio)

    # Start the trading bot
    trader.start()

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' and 'YOUR_API_SECRET' with your actual Binance API credentials
    api_key: str = 'YOUR_API_KEY'
    api_secret: str = 'YOUR_API_SECRET'
    print('lets BEGIN:\n\n\n')
    main(api_key, api_secret)
