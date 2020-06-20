from faker import Faker
fake = Faker()

class baseContact:
    def __init__ (self, name_and_surname, telephone_number, email):
        self.name_and_surname = fake.name(),
        self.telephone_number = telephone_number
        self.email = email

class BusinessContact(baseContact):
    def __init__(self, position, company, business_number):
        super().__init__(*args, **kwargs)
        