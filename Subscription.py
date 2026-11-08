from abc import ABC, abstractmethod

class Subscription(ABC):
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price

    @abstractmethod
    def calculate_price(self) -> float:
        pass

    @abstractmethod
    def can_attend(self) -> bool:
        pass

    @abstractmethod
    def use_entry(self) -> None:
        pass
