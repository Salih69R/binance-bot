from abc import ABCMeta, abstractmethod

class ITradingStrategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, symbol: str) -> None:
        pass
