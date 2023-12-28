from contextlib import contextmanager

@contextmanager
def context_string(string_input):
    print("Otworzenie managera funkcyjnego...\n")
    swapped = string_input.swapcase()
    try:
        yield swapped
    except ValueError as ve:
        print(f'błąd poboru danych... {ve}\n')
    finally:
        print("zamknięcie działania...\n")

    print("koniec działania contextmanagera")


with context_string('wielkie i ważne wydarzenie dnia: wschód SŁOŃCA...') as sws:
    print(sws)
