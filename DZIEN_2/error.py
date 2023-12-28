try:
    # x =4
    print(x)
except NameError:
    print("x nie jest zdefiniowany")
except TypeError:
    print("niewłaściwa wartość")
except:
    print("nieoczekiwany błąd!")
else:
    print(f'podwójny x = {2*x}')
finally:
    v = 9
    print(f'ostatnia składowa instrukcji try-except, wypisanie wartości v = {v}')

print("ciąg dalszy programu...")


if 'y' in locals() and y is not None:
    print("Zmienna istnieje i nie jest None.")
else:
    print("Zmienna nie istnieje lub jest None.")
