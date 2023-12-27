liczby = [56,90,88,100,-45,-67,0,2,0,190,-133,987,-456,92,34,-55,-145,600,-300,2,5,6]

# liczby2 = [3,3,3,3,3,3,3,3,3,3,3,3]

def pokaz_statystyki(lista):
    minimum = min(lista)
    maksimum = max(lista)
    rozstep = maksimum - minimum
    liczba_el = len(lista)
    suma_el = sum(lista)
    sr_arytm = suma_el/liczba_el
    return minimum,maksimum,rozstep,liczba_el,suma_el,sr_arytm
wynik = pokaz_statystyki(liczby)
print(wynik)
print(type(wynik))

mini, maxi, roz , le, se, srednia = pokaz_statystyki(liczby)
print(f'wartość największa :{maxi}, wartość najmniejsza: {mini}, rozstęp: {roz}, liczba elementów {le},'
      f'suma wszystkich elementów: {se}, średnia arytmetyczna: {srednia:.3f}')

