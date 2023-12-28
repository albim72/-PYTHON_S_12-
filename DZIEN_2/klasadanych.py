from dataclasses import dataclass,astuple,asdict,field

@dataclass
class Book:
    id:int
    tytul:str
    autor:str
    lstron:int
    def __init__(self,wydawnictwo):
        self.wydawnictwo = wydawnictwo
        

# b1 = Book(34,"Biegi Górskie","Anna Kawka",330)
# print(f'tytuł: {b1.tytul}')

b2 = Book("ABC")

print("_"*50)

@dataclass
class Person:
    city:str
    firstname:str = "Janusz"
    lastname:str = "Kot"
    age:int = 53
    job:str = "Data Developer"
    full_name:str = field(init=False,repr=False)

    def __repr__(self):
        return f'Pracownik {self.firstname} {self.lastname}, stanowisko: {self.job}'

    def __post_init__(self):
        self.full_name = self.firstname + " " + self.lastname


os1 = Person("Kraków")
print(os1)
print(os1.full_name)

os2 = Person("Lublin","Olga","Nowak",27,"Dyrektor")
print(os2)
print(os2.full_name)

print(astuple(os1))
print(asdict(os2))
