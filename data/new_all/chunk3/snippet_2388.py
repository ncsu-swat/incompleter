# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47103106/python3-subclass-is-being-instantiated-as-superclass-subclass-method-not-found
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pydealer
    _l_(551413)

except ImportError:
    pass

class Hand(_a_(551415, _n_(551414, "pydealer", lambda: pydealer), "Stack")):
    _l_(551480)


    stay = None
    _l_(551416)
    showfirstcard = None
    _l_(551417)
    bust = None
    _l_(551418)

    def __init__(self, showfirst, **kwargs):
        _l_(551428)

        _c_(551422, _a_(551420, _n_(551419, "super", lambda: super)(), "__init__"), **_n_(551421, "kwargs", lambda: kwargs))
        _l_(551423)
        stay = False
        _l_(551424)
        _n_(551425, "self", lambda: self).showfirstcard = _n_(551426, "showfirst", lambda: showfirst)
        _l_(551427)

    def stackscore(self):
        _l_(551450)

        total = 0
        _l_(551429)
        for card in _n_(551430, "self", lambda: self):
            _l_(551436)

            total += _c_(551434, _a_(551432, _n_(551431, "self", lambda: self), "__bjval"), _n_(551433, "card", lambda: card))
            _l_(551435)
        if _n_(551437, "total", lambda: total) > 21:
            _l_(551447)

            for card in _n_(551438, "self", lambda: self):
                _l_(551446)

                if _a_(551440, _n_(551439, "card", lambda: card), "value") == "Ace":
                    _l_(551442)

                    total -= 10
                    _l_(551441)
                if _n_(551443, "total", lambda: total) <= 21:
                    _l_(551445)

                    break
                    _l_(551444)
        aux = _n_(551448, "total", lambda: total)
        _l_(551449)
        return aux

    def __bjval(self, card):
        _l_(551454)

        aux = {
                '2': 2,
                '3': 3,
                '4': 4,
                '5': 5,
                '6': 6,
                '7': 7,
                '8': 8,
                '9': 9,
                '10': 10,
                'Jack': 10,
                'Queen': 10,
                'King': 10,
                'Ace':11
                }[_a_(551452, _n_(551451, "card", lambda: card), "value")]
        _l_(551453)
        return aux

    def setstay(self):
        _l_(551457)

        _n_(551455, "self", lambda: self).stay = True
        _l_(551456)

    def getsize(self):
        _l_(551462)

        aux = _c_(551460, _a_(551459, _n_(551458, "self", lambda: self), "size"))
        _l_(551461)
        return aux

    def showcards(self):
        _l_(551479)

        for i, card in _c_(551465, _n_(551463, "enumerate", lambda: enumerate), _n_(551464, "self", lambda: self)):
            _l_(551478)

            if _n_(551466, "i", lambda: i) == 0:
                _l_(551477)

                if _a_(551468, _n_(551467, "self", lambda: self), "showfirstcard") == False:
                    _l_(551476)

                    _c_(551470, _n_(551469, "print", lambda: print), '***FACEDOWN CARD***')
                    _l_(551471)
                else:
                    _c_(551474, _n_(551472, "print", lambda: print), _n_(551473, "card", lambda: card))
                    _l_(551475)