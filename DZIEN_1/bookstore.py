class Osoba:
    def __init__(self,imie,wiek,waga,wzrost):
        self.imie = imie
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost
        self.koloroczu = "brązowe"
        self.newosoba()

    def newosoba(self):
        print("utworzenie nowego obiektu klasy Osoba!")

    def print_osoba(self):
        print(f'osoba -> imię: {self.imie}, wiek: {self.wiek}, waga: {self.waga} kg, '
              f'wzrost: {self.wzrost} cm, kolor oczu: {self.koloroczu}')

    def czypracownik(self):
        return False



os1 = Osoba("Jan",34,101,180)
os1.print_osoba()
print(f"czy osoba jest pracownikiem?({os1.czypracownik()})")

class Firma:
    def __init__(self,nazwa,branza,miasto):
        self.nazwa = nazwa
        self.branza = branza
        self.miasto = miasto
        
    def show_firma(self):
        print(f'firma: {self.nazwa}({self.branza}) - miasto: {self.miasto}')
        
