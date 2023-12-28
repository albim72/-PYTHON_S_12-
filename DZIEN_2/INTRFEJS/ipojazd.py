from abc import ABCMeta,abstractmethod

class IPojazd(metaclass=ABCMeta):
    @abstractmethod
    def spalanie(self,odl,litry):raise NotImplementedError

    @abstractmethod
    def kosztyprzejazdu(self,odl,litry,cena):raise NotImplementedError
