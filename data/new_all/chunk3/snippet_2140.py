# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61651817/i-am-getting-type-error-in-multiple-inheritance-in-python-opp
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import  random
    _l_(530562)

except ImportError:
    pass


class Coin:
    _l_(530582)

    def flip(self):
        _l_(530577)

        #toss=int(input('how many times you want to tosses the coin?: '))
        for i in _c_(530565, _n_(530563, "range", lambda: range), _n_(530564, "self", lambda: self)):
            _l_(530576)

            rand=_c_(530568, _a_(530567, _n_(530566, "random", lambda: random), "randint"), -1,1)
            _l_(530569)
            if _n_(530570, "rand", lambda: rand)==1:
                _l_(530575)

                aux = _n_(530571, "rand", lambda: rand)
                _l_(530572)
                return aux
            else:
                aux = _n_(530573, "rand", lambda: rand)
                _l_(530574)
                return aux
                #print('tail')
    _c_(530580, _n_(530578, "print", lambda: print), _c_(530579, flip, 4))
    _l_(530581)

class Dice:
    _l_(530598)

    def roll(self):
        _l_(530593)

        #x=int(input("inter number"))
        for x in _c_(530585, _n_(530583, "range", lambda: range), _n_(530584, "self", lambda: self)):
            _l_(530592)

            points=_c_(530588, _a_(530587, _n_(530586, "random", lambda: random), "randint"), 1,6)
            _l_(530589)
            aux = _n_(530590, "points", lambda: points)
            _l_(530591)
            return aux
    _c_(530596, _n_(530594, "print", lambda: print), _c_(530595, roll, 5))
    _l_(530597)

class Player(_n_(530599, "Coin", lambda: Coin),_n_(530600, "Dice", lambda: Dice)):
    _l_(530616)

    def rolls(self):
        _l_(530611)

        # x=int(input("inter number"))
        for x in _c_(530603, _n_(530601, "range", lambda: range), _n_(530602, "self", lambda: self)):
            _l_(530610)

            points = _c_(530606, _a_(530605, _n_(530604, "random", lambda: random), "randint"), 1, 6)
            _l_(530607)
            aux = _n_(530608, "points", lambda: points)
            _l_(530609)
            return aux

    _c_(530614, _n_(530612, "print", lambda: print), _c_(530613, rolls, 5))
    _l_(530615)


obj=_c_(530618, _n_(530617, "Player", lambda: Player))
_l_(530619)
_c_(530622, _a_(530621, _n_(530620, "obj", lambda: obj), "flip"))
_l_(530623)
_c_(530626, _a_(530625, _n_(530624, "obj", lambda: obj), "roll"))
_l_(530627)