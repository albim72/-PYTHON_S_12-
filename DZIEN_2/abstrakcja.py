from abc import ABC,abstractmethod

class Prototyp(ABC):
    def __init__(self,x):
        self.x=x

    def msg(self,info):
        return f"informacja: {info}"

    @abstractmethod
    def policz(self):
        pass

    @abstractmethod
    def policz_x(self):
        return self.x*7


class Regular(Prototyp):

    def __init__(self, x,y):
        super().__init__(x)
        self.y=y

    def policz(self):
        return 1004

    def policz_x(self):
        return super().policz_x() + self.y*2


re= Regular(4,6)
print(f'metoda policz() -> {re.policz()}')
print(f'metoda policz_x() -> {re.policz_x()}')
print(f'ważne... {re.msg("AAA444a")}')
