#funkcja silnia: n! = 1*2*3*...*n
#górna granica typu double -> 1.8E+308
# n??? n=171
#dziedzina funkcji (n>=0)

import sys
from silniaerr import SilniaError

sys.set_int_max_str_digits(0x10000000)
def silnia(n):
    if n<0:
        raise SilniaError(n)
    wynik=1
    for i in range(1,n+1):
        wynik *= i
    return wynik

try:
    n = int(input("podaj wartość argumentu n funkcji silnia: "))
    print(f'wynik funkcji silnia dla n={n} wynosi: {silnia(n)}')
except SilniaError as info:
    print(info)







