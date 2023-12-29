class Adres:
    def __init__(self,ulica,miasto,kraj):
        self.ulica = ulica
        self.miasto = miasto
        self.kraj = kraj

class Osoba:
    def __init__(self,imie,nazwisko,adres:Adres):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adres


class Pracownik:
    def __init__(self,imie,nazwisko,adres,id_prac):
        self.osoba = Osoba(imie,nazwisko,adres)
        self.id_prac = id_prac


adr = Adres("Złota 6, 12-457","Kraków","Polska")
prc = Pracownik("Jan","Kot",adr,353)

print(prc.osoba.imie)
print(prc.osoba.adres.miasto)
print(prc.id_prac)





