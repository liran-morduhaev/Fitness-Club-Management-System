from Person import Person

class Member(Person):
    def __init__(self, phone, name, person_id):
        super().__init__(phone, name, person_id)
        self._balance = 0.0
        self.__attendance_count = 0
        self.subscription = None

    @property
    def balance(self):
        return self._balance

    @property
    def attendance_count(self):
        return self.__attendance_count

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def deduct_funds(self, amount):
        if amount < 0:
            raise ValueError(f'Your balance too low for this action')
        else:
            self._balance -= amount

    def record_attendance(self):
        self.__attendance_count += 1

