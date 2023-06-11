from binance.client import Client
from strategy.ITradingStrategy import ITradingStrategy
from portfolio.MyPortfolio import MyPortfolio

class MyTrader:
    def __init__(self, client: Client, strategy: ITradingStrategy, portfolio: MyPortfolio) -> None:
        self.client = client
        self.strategy = strategy
        self.portfolio = portfolio

    def start(self) -> None:
        # Implement the main trading loop here
        self.step()
        pass

    def step(self) -> None:
        self.portfolio.get_balance('BTC')