from Subscription import Subscription

class MonthlySubscription(Subscription):
    def __init__(self, base_price: float = 200.0):
        super().__init__("Monthly Member", base_price)

    def can_attend(self) -> bool:
        return True

    def use_entry(self) -> None:
        pass

    def calculate_price(self) -> float:
        return self.base_price


