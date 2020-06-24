from faker import Faker
fake = Faker()

class BaseContact:
    def __init__ (self, name_and_surname, number, email):
        self.name_and_surname = name_and_surname
        self.number = number
        self.email = email

    def __str__ (self):
        return f'{self.name_and_surname} {self.number} {self.email}'

    def __repr__(self):
        return f"baseContact(name_and_surname={self.name_and_surname}, phone_number={self.phone_number}, email_address={self.email_address})"

    def contact(self):
        return f"Wybieram numer {self.number} i dzwonię do {self.name_and_surname}"

    @property
    def label_length(self):
        return sum([len(self.first_name), len(self.last_name), 1])
    
class BusinessContact(BaseContact):
    def __init__(self, position, company, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        
    def __str__(self):
        return f'{self.position} {self.company} {self.number}'

    def __repr__(self):
        return f"BusinessContact(company={self.company} position={self.position} business_number={self.number})"

    def contact_business(self):
        return (f"Wybieram numer {self.number} i dzwonię do {self.name_and_surname}")

def create_contacts(card, quantity):
    for i in range(quantity):
        list_of_cards = []
        if card == "private":
            card = BaseContact(fake.name(), fake.phone_number(), fake.email())
            list_of_cards.append(card)
        elif card == "business":
            card = BusinessContact(fake.name(), fake.phone_number(), fake.email(), fake.job(), fake.company()) 
            list_of_cards.append(card)   
        else:
            exit(1)
    return list_of_cards

print("private", 5)
print(list_of_cards, "private")