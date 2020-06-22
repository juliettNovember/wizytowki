from faker import Faker
fake = Faker("pl_PL")

class BaseContact:
    def __init__ (self, name_and_surname, number, email):
        self.name_and_surname = name_and_surname
        self.number = number
        self.email = email

    def __str__ (self):
        return f'{name_and_surname} {number} {email}'

    def __repr__(self):
        return f"baseContact(name_and_surname={self.name_and_surname}, phone_number={self.phone_number}, email_address={self.email_address})"

    def contact(self):
        return f"Wybieram numer {self.number} i dzwonię do {self.name_and_surname}"

@property
def label_length(self):
    return sum([len(self.first_name), len(self.last_name), 1])
    
class BusinessContact(BaseContact):
    def __init__(self, position, company, business_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.business_number = business_number

    def __str__(self):
        return f'{position} {company} {business_number}'

    def __repr__(self):
        return f"BusinessContact(company={self.company} position={self.position} business_number={self.business_number})"

    def contact_business(self):
        return f"Wybieram numer {self.business_number} i dzwonię do {self.name_and_surname}"

@property
def label_length(self):
    return sum([len(self.name_and_surname)])

person = BusinessContact(name_and_surname = fake.name_and_surname(), number = fake.number(), email = fake.email(), position = fake.position(), company = fake.company(), business_number = fake.business_number())

card = ("private", "business")
quantity = 3
contact = ""
random_card = []

def create_contacts(card, quantity):
    if type == "private":
        for i in range(quantity):
            contact = f"{fake.name_and_surname()}, {fake.number()}, {fake.email()}"
            random_card.append(contact)
    elif type == "business":
        for i in range (quantity):
            contact = f"{fake.name_and_surname()}, {fake.business_number()}, {fake.email()}, {fake.position()}, {fake.company()}"
            random_card.append(contact)
    else:
        exit(1)
    return random_card


print(create_contacts("business"))