class Departament:
    def __init__(self,nazwa_dep,pracownicy):
        self.nazwa_dep = nazwa_dep
        self.pracownicy = pracownicy


class Pracownik:
    def __init__(self,imie,nazwisko,departament):
        self.imie = imie
        self.nazwisko = nazwisko
        self.departament = departament



departament = Departament("IT",[])
prac1 = Pracownik("Olga","Knot",departament)
prac2 = Pracownik("Antek","Nowak",departament)
departament.pracownicy.append(prac1)
departament.pracownicy.append(prac2)

print(departament.nazwa_dep)
print(len(departament.pracownicy))
print(departament.pracownicy[0].nazwisko)
print(departament.pracownicy[1].nazwisko)


