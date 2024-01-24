# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50591953/typeerror-not-supported-between-instances-of-printer-and-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
products = {

    "A": [100, "cola"],
    "B": [100, "drink0"]

}
_l_(472943)


def coinCounter():
    _l_(472952)

    _c_(472945, _n_(472944, "print", lambda: print), "Bitte Münzen einwerfen! / Betrag eingeben!")
    _l_(472946)

    credits = _c_(472950, _n_(472947, "int", lambda: int), _c_(472949, _n_(472948, "input", lambda: input), "Betrag: "))
    _l_(472951)


def product():
    _l_(473004)

    _c_(472954, _n_(472953, "print", lambda: print), "Bitte Produkt wählen!")
    _l_(472955)

    choosedProduct = _c_(472959, _a_(472958, _c_(472957, _n_(472956, "input", lambda: input), "Produkt: "), "capitalize"))
    _l_(472960)

    if _n_(472961, "choosedProduct", lambda: choosedProduct) in _n_(472962, "products", lambda: products) and _n_(472963, "credits", lambda: credits) >= _n_(472964, "products", lambda: products)[_n_(472965, "choosedProduct", lambda: choosedProduct)][0]:
        _l_(472980)

        output = True
        _l_(472966)
    elif _n_(472967, "choosedProduct", lambda: choosedProduct) not in _n_(472968, "products", lambda: products):
        _l_(472979)

        _c_(472970, _n_(472969, "print", lambda: print), "Das Produkt existiernt nicht.")
        _l_(472971)
    elif _n_(472972, "products", lambda: products)[_n_(472973, "choosedProduct", lambda: choosedProduct)][0] >= _n_(472974, "credits", lambda: credits):
        _l_(472978)

        _c_(472976, _n_(472975, "print", lambda: print), "Du hast nicht genug Geld eingeworfen")
        _l_(472977)

    def moneyBack(moneyBack):
        _l_(472989)

        moneyBack = _n_(472981, "credits", lambda: credits) - _n_(472982, "products", lambda: products)[_n_(472983, "choosedProduct", lambda: choosedProduct)][0]
        _l_(472984)
        _c_(472987, _n_(472985, "print", lambda: print), "Zurück: ", _n_(472986, "moneyBack", lambda: moneyBack))
        _l_(472988)


    def output(output, choosedProduct):
        _l_(472997)

        if _n_(472990, "output", lambda: output) == True:
            _l_(472996)

            _c_(472993, _n_(472991, "print", lambda: print), "Das Produkt", _n_(472992, "choosedProduct", lambda: choosedProduct)[1], "wird ausgegeben...")
            _l_(472994)
            output = False
            _l_(472995)

    _c_(472999, _n_(472998, "output", lambda: output))
    _l_(473000)
    _c_(473002, _n_(473001, "moneyBack", lambda: moneyBack))
    _l_(473003)



def main():
    _l_(473011)

    _c_(473006, _n_(473005, "coinCounter", lambda: coinCounter))
    _l_(473007)
    _c_(473009, _n_(473008, "product", lambda: product))
    _l_(473010)

_c_(473013, _n_(473012, "main", lambda: main))
_l_(473014)