from faker import Faker
fake = Faker()

card = ""

class baseContact:
    def __init__ (self, name_and_surname, number, email):
        self.name_and_surname = fake.name()
        self.number = fake.number()
        self.email = fake.email()
base = baseContact(name_and_surname = fake.name(), number = fake.number(), email = fake.email())

card_list = []
for i in range(5):
    card = (f"{fake.number()}, {fake.name_and_surname()}")
    card_list.append(card)

class BusinessContact(baseContact):
    def __init__(self, position, company, business_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.business_number = business_number

business = BusinessContact(position = fake.job(), company = fake.company(), business_number = fake.business_number())


print(card)


