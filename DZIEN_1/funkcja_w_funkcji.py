#przykład 1

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

    def brak():
        return "brak wpłaty - masz 3 dni na uzupełnienie!"

    def error():
        return "błąd w rejestracji: 1 - opłacono, 2 - nieopłacono, inna wartość -> błąd!"

    if oplata == 1:
        return lista_zawodnikow
    elif oplata == 0:
        return brak
    else:
        return error


print(rejestracja(1)(56))
print(rejestracja(0)())
print(rejestracja(56)())
