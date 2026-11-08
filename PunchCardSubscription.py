from Subscription import Subscription

class PunchCardSubscription(Subscription):
    def __init__(self, entries: int = 10, base_price: float = 150.0):
        super().__init__("Punch Card",base_price)
        self.remaining_entries = entries

    def calculate_price(self) -> float:
        return self.base_price

    def can_attend(self) -> bool:
        return self.remaining_entries > 0

    def use_entry(self) -> None:
        if not self.can_attend():
            raise ValueError("No entries remaining.")
        self.remaining_entries -= 1
