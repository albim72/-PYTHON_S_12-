from oblicz import Obliczenia
from daty import Dates
from mtekst import MojTekst

print(f"wartość wynosi: {Obliczenia.moblicz(2,7,5)}")

o1 = Obliczenia(4,3,2)
print(o1.moblicz(6,6,6))

date = Dates("13-12-2016")
datefromdb = "13/12/2019"

datewd = Dates.to_dash_date(datefromdb)
d1 = date.get_date()
d2 = datewd

if (d1==d2):
    print(f"Identyczne daty -> d1 {d1}, d2 {d2}")
else:
    print(f"Różne daty -> d1 {d1}, d2 {d2}")

mt = MojTekst("dane do pobrania")
print(mt.msg())
print(mt.opis("konkretne dane: abc"))
print(MojTekst.opis("to jest statyczne"))
