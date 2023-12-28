def dzielenie(x,y):
    try:
        wynik = x/y
    except ZeroDivisionError:
        print("nie dziel przez 0!")
    except NameError:
        print("zmienne niezdefiniowane")
    except TypeError as bb:
        print(f"Błąd: {bb}")
    except Exception as ex:
        print(f"komunikat błędu: {ex}")
    else:
        print(f'wynik = {wynik}')
    finally:
        print("policzmy coś jeszcze!")

try:
    dzielenie(3,4)
    dzielenie(3,0)
    dzielenie(0,0)
    dzielenie(-0.0045343533,4)
    dzielenie(True,67)
    dzielenie(2424424242,0.08)
    dzielenie(3,"rity")
    dzielenie(56)
except TypeError as g:
    print(f"zbyt mało argumentów -> podaj (x,y): {g}")
