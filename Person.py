class Person:
    def __init__(self, phone, name, person_id):
        self.phone = phone
        self.name = name
        self.person_id = person_id

    def get_details(self):
        return f'Person name: {self.name}, phone number: {self.phone} '