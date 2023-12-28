from ipojazd import IPojazd

class Pojazd(IPojazd):
    def spalanie(self, odl, litry):
        return litry*100/odl

    def kosztyprzejazdu(self, odl, litry, cena):
        return self.spalanie(odl,litry)*(odl/100)*cena
