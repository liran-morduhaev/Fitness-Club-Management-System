from Person import Person

class Trainer(Person):
    def __init__(self, phone, name, person_id, specialty, hourly_rate):
        super().__init__(phone, name, person_id)
        self.specialty = specialty
        self.hourly_rate = hourly_rate

        

