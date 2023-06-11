# my_portfolio.py

from binance.client import Client
from binance.exceptions import BinanceAPIException
from typing import Dict, Optional

class MyPortfolio:
    def __init__(self, client: Client) -> None:
        self.client = client

    def get_balance(self, symbol: str) -> Optional[float]:
        try:
            account_info = self.client.get_account()
        except BinanceAPIException as e:
            print("Failed to retrieve account info:", e)
            return None

        balances = {item['asset']: float(item['free']) for item in account_info['balances']}
        if symbol in balances:
            return balances[symbol]
        else:
            print("Symbol", symbol, "not found in the account.")
            return None

    def execute_trade(self, symbol: str, side: str, quantity: float) -> bool:
        try:
            self.client.create_order(
                symbol=symbol,
                side=side,
                type='MARKET',
                quantity=quantity
            )
        except BinanceAPIException as e:
            print("Failed to execute trade:", e)
            return False

        return True
