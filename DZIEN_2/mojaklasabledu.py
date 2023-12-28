class MyCustomError(Exception):
    def __init__(self,*args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print("komunikat błędu!")
        if self.message:
            return f"{self.__class__.__name__} -> {self.message}"
        else:
            return f"{self.__class__.__name__} -> brak wiadmości błędu"


def info(n=None):
    if n:
        print(f'bardzo ważna wiadmość:{n}')
    else:
        raise MyCustomError("brak ważnej wiadomości...")


try:
    info("sdfsfgsdf")
    info()
except MyCustomError as mc:
    print(mc)
