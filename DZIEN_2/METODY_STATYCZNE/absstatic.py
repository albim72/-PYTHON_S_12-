from abc import ABC, abstractmethod

class Tekst(ABC):

    def __init__(self,t):
        self.t=t

    # @staticmethod
    @abstractmethod
    def opis(info):pass

    @abstractmethod
    def msg(self):pass
