#przykład 1
import math


def witaj(imie):
    return f"dziękujemy za założenie konta: {imie}"

def konkurs(imie,punkty,laureat):
    if punkty>80:
        return f"osoba {imie}, liczba punktów: {punkty} jest {laureat} konkursu"
    else:
        return f"osoba {imie}, jest {laureat} konkursu"

def bonus(punkty,premia):
    if punkty < 30:
        return punkty - premia
    elif punkty < 60:
        return punkty
    else:
        return punkty+premia

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))

print(osoba(konkurs,"Anna",90,"laureatem"))
print(osoba(konkurs,"Olaf",33,"uczestnikiem"))

print(osoba(bonus,66,10))
print(osoba(bonus,45,10))
print(osoba(bonus,12,10))


#przykład 2

def rejestracja(oplata):
    def lista_zawodnikow(nr):
        return f"jesteś na liście zawodników nr {nr}- opłata wniesiona!"

    def brak(rodzaj):
        return f"brak wpłaty, rodzaj - {rodzaj}- masz 3 dni na uzupełnienie!"

    def error():
        return "błąd w rejestracji: 1 - opłacono, 2 - nieopłacono, inna wartość -> błąd!"

    if oplata == 1:
        return lista_zawodnikow
    elif oplata == 0:
        return brak
    else:
        return error

print(rejestracja(1)(56))
print(rejestracja(0)("karta maestro"))
print(rejestracja(56)())


#przykład 3

def startstop(funkcja):
    def wrapper(*args):
        print("początek procesu...")
        funkcja(*args)
        print("koniec procesu...")
    return wrapper

def zawijanie(czego):
    print(f"zawijanie {czego} w sreberka")

zw = startstop(zawijanie)
print("_"*60)
zw("czekoladek")

print("_"*60)


@startstop
def dmuchanie(czego):
    print(f"dmuchanie {czego} na urodzinowym torcie")

dmuchanie("świeczek")
print("_"*60)
@startstop
def f(x):
    print(2*x)

def g(x):
    return x-3

f(99)
print("_"*60)
print(g(0))

#dekorator policz

def policz(funkcja):
    def wrapper(*args):
        print("podstawienie funkcji f(x) i pierwiastek z jej wyniku")
        print(f"wynik: {math.sqrt(funkcja(*args))}")
    return wrapper

@policz
def suma(a,b):
    return a + b

@policz
def podiloczyn(x,y):
    return 2*x*y

suma(5,6)
podiloczyn(6,7)

