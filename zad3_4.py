# ksiazka adresowa dane wprowadzic usunac i zmodyfikowac, wyswietlane w postaci tabeli
# imie nazwisko adres kraj nr tel email

class User():
    def __init__(self, name, country, adress, phone, email):
        self.name = name
        self.country = country
        self.adress = adress
        self.phone = phone
        self.email = email



u=[]
u.append(User('Adam', 'Polska', 'Adressssss', 123123123, 'email'))

print u[0].__dict__
