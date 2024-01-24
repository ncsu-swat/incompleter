# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62971435/learning-inheritance-typeerror-init-takes-3-positional-arguments-but-5
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class BasicToken:
    _l_(678026)


    asset_class = "Crypto-Currency"
    _l_(678021)

    def __init__(self, symbol):
        _l_(678025)

        _n_(678022, "self", lambda: self).symbol = _n_(678023, "symbol", lambda: symbol)
        _l_(678024)


class StableCoin(_n_(678027, "BasicToken", lambda: BasicToken)):
    _l_(678035)

    def __init__(self, color, supply):
        _l_(678034)

        _n_(678028, "self", lambda: self).color = _n_(678029, "color", lambda: color)
        _l_(678030)
        _n_(678031, "self", lambda: self).supply = _n_(678032, "supply", lambda: supply)
        _l_(678033)

icon = _c_(678037, _n_(678036, "BasicToken", lambda: BasicToken), 'icx')
_l_(678038)
icxStable = _c_(678040, _n_(678039, "StableCoin", lambda: StableCoin), 'DMM', ['Blue', 'White'])
_l_(678041)

_c_(678045, _n_(678042, "print", lambda: print), 'Icon Symbol: '+ _a_(678044, _n_(678043, "icon", lambda: icon), "symbol"))
_l_(678046)
_c_(678050, _n_(678047, "print", lambda: print), 'IcxStable Symbol: '+ _a_(678049, _n_(678048, "icxStable", lambda: icxStable), "symbol"))
_l_(678051)