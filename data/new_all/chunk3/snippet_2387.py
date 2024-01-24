# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47103106/python3-subclass-is-being-instantiated-as-superclass-subclass-method-not-found
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from hand.py import Hand
    _l_(576222)

except ImportError:
    pass

class Player:
    _l_(576271)


    hands = []
    _l_(576223)
    __chips = None
    _l_(576224)
    __betamount = None
    _l_(576225)

    def __init__(self):
        _l_(576228)

        _n_(576226, "self", lambda: self).__chips = 5000
        _l_(576227)

    def bet(self):
        _l_(576234)

        _c_(576232, _n_(576229, "type", lambda: type), _a_(576231, _n_(576230, "self", lambda: self), "__betamount"))
        _l_(576233)

    def __deal(self, twocards):
        _l_(576248)

        _n_(576235, "self", lambda: self).hands = [_c_(576237, _n_(576236, "Hand", lambda: Hand), showfirst=True)]
        _l_(576238)
        _a_(576240, _n_(576239, "self", lambda: self), "hands")[0] += _n_(576241, "twocards", lambda: twocards)
        _l_(576242)
        _c_(576246, _a_(576245, _a_(576244, _n_(576243, "self", lambda: self), "hands")[0], "showcards"))
        _l_(576247)

    def hit(self, card, whichhand):
        _l_(576254)

        _a_(576250, _n_(576249, "self", lambda: self), "hands")[_n_(576251, "whichhand", lambda: whichhand)] += _n_(576252, "card", lambda: card)
        _l_(576253)

    def stay(self, whichhand):
        _l_(576261)

        _c_(576259, _a_(576258, _a_(576256, _n_(576255, "self", lambda: self), "hands")[_n_(576257, "whichhand", lambda: whichhand)], "setstay"))
        _l_(576260)

    def printscore(self, whichhand):
        _l_(576270)

        _c_(576268, _n_(576262, "print", lambda: print), _c_(576267, _a_(576266, _a_(576264, _n_(576263, "self", lambda: self), "hands")[_n_(576265, "whichhand", lambda: whichhand)], "stackscore")))
        _l_(576269)