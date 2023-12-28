from absstatic import Tekst

class MojTekst(Tekst):
    @staticmethod
    def opis(info):
        return f"informacja: {info}"

    def msg(self):
        return 4*self.t
