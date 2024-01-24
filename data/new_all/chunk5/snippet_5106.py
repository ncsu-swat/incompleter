# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62971435/learning-inheritance-typeerror-init-takes-3-positional-arguments-but-5
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class BasicToken:
    _l_(692261)


    asset_class = "Crypto-Currency"
    _l_(692256)

    def __init__(self, symbol):
        _l_(692260)

        _n_(692257, "self", lambda: self).symbol = _n_(692258, "symbol", lambda: symbol)
        _l_(692259)


class StableCoin(_n_(692262, "BasicToken", lambda: BasicToken)):
    _l_(692270)

    def __init__(self, color, supply):
        _l_(692269)

        _n_(692263, "self", lambda: self).color = _n_(692264, "color", lambda: color)
        _l_(692265)
        _n_(692266, "self", lambda: self).supply = _n_(692267, "supply", lambda: supply)
        _l_(692268)

icon = _c_(692272, _n_(692271, "BasicToken", lambda: BasicToken), 'icx')
_l_(692273)
icxStable = _c_(692275, _n_(692274, "StableCoin", lambda: StableCoin), 'DMM', ['Blue', 'White'])
_l_(692276)

_c_(692280, _n_(692277, "print", lambda: print), 'Icon Symbol: '+ _a_(692279, _n_(692278, "icon", lambda: icon), "symbol"))
_l_(692281)
_c_(692285, _n_(692282, "print", lambda: print), 'IcxStable Symbol: '+ _a_(692284, _n_(692283, "icxStable", lambda: icxStable), "symbol"))
_l_(692286)