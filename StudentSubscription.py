from overrides import overrides
from MonthlySubscription import MonthlySubscription

class StudentSubscription(MonthlySubscription):
    def __init__(self, base_price: float = 200.0, discount_rate: float = 0.2):
        super().__init__(base_price)
        self.discount_rate = discount_rate

    @overrides
    def calculate_price(self) -> float:
        return self.base_price * (1 - self.discount_rate)