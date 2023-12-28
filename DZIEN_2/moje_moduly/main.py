# import dane
# import dane as dn
from dane import nrfilii as filia
from dane import book as bk
# import dane
# import dane as dn
from dane import nrfilii as filia
from dane import book as bk

from funkcje.bfunkcje import czytaj_liste,czytaj_slownik

print("________________ wyświetalnie bezpośrednio ____________________")
print(filia)
print(bk)

print("________________ wyświetalnie za pomocą funkcji ____________________")
czytaj_liste(filia)
czytaj_slownik(bk)
