class Book:
    def __new__(cls, *args, **kwargs):
        return object.__new__(Book)

    def __init__(self,id,tytul,autor,cena=30):
        self.id = id
        self.tytul = tytul
        self.autor = autor
        self.cena = cena
        self.oprawa = "miękka"

    def __repr__(self):
        return f"książka {self.tytul}, autor: {self.autor}, cena: {self.cena} zł"

    def __call__(self,wydawnictwo):
        print(f"wydawnictwo: {wydawnictwo}")
        print(f"kwota do zapłaty: {self.cena - self.rabat(14):.2f} zł")

    def rabat(self,procent):
        return self.cena*(procent/100)

    def get_oprawa(self):
        return self.oprawa

    def set_oprawa(self,nowaoprawa):
        self.oprawa = nowaoprawa


    @property
    def cena(self):
        return self._cena

    @cena.setter
    def cena(self,nowacena):
        self._cena = nowacena



bk1 = Book(45,"Wiedźmin","Andrzej Sapkowski",43)
print(bk1.autor)
bk1.cena = 50
print(f"zmieniono cenę książki na {bk1.cena} zł")
print(bk1)
bk1("MyBook")
print(f'rabat: {bk1.rabat(14):.2f} zł')
bk1.set_oprawa("twarda")
print(f"oprawa: {bk1.get_oprawa()}")

print("_"*60)

bk2 = Book(67,"Hobbit","J.R.R. Tolkien",40)
print(bk2)
bk2("Orion")
print(f'rabat: {bk2.rabat(14):.2f} zł')
bk2.set_oprawa("twarda")
print(f"oprawa: {bk2.get_oprawa()}")
print(f"cena przed rabatem: {bk2.cena} zł")


