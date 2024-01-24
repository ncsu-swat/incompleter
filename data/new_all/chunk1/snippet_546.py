# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49472108/typeerror-not-supported-between-instances-of-list-and-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
million = [1000000, "M"]
_l_(401071)
billion = [_n_(401072, "million", lambda: million) * 1000, "B"]
_l_(401073)
trillion = [_n_(401074, "billion", lambda: billion) * 1000, "T"]
_l_(401075)
quadrillion = [_n_(401076, "trillion", lambda: trillion) * 1000, "Qd"]
_l_(401077)
quintillion = [_n_(401078, "quadrillion", lambda: quadrillion) * 1000, "Qn"]
_l_(401079)
sx = [_n_(401080, "quintillion", lambda: quintillion) * 1000, "Sx"]
_l_(401081)
septillion = [_n_(401082, "sx", lambda: sx) * 1000, "Sp"]
_l_(401083)

suffixes = [_n_(401084, "million", lambda: million), _n_(401085, "billion", lambda: billion), _n_(401086, "trillion", lambda: trillion), _n_(401087, "quadrillion", lambda: quadrillion), _n_(401088, "quintillion", lambda: quintillion), _n_(401089, "sx", lambda: sx), _n_(401090, "septillion", lambda: septillion)]
_l_(401091)

def getSetupResult(orevalue, furnacemultiplier, *upgrades, **kwargs):
    _l_(401112)

    for i in _n_(401092, "upgrades", lambda: upgrades):
        _l_(401095)

        orevalue *= _n_(401093, "i", lambda: i)
        _l_(401094)
    orevalue *= _n_(401096, "furnacemultiplier", lambda: furnacemultiplier)
    _l_(401097)
    for suffix in _n_(401098, "suffixes", lambda: suffixes):
        _l_(401111)

        if _n_(401099, "orevalue", lambda: orevalue) > _n_(401100, "suffix", lambda: suffix)[0] - 1 and _n_(401101, "orevalue", lambda: orevalue) < _n_(401102, "suffix", lambda: suffix)[0] * 1000:
            _l_(401110)

            _c_(401108, _n_(401103, "print", lambda: print), "$"+_c_(401106, _n_(401104, "str", lambda: str), _n_(401105, "orevalue", lambda: orevalue))+_n_(401107, "suffix", lambda: suffix)[1])
            _l_(401109)

_c_(401115, _n_(401113, "getSetupResult", lambda: getSetupResult), _n_(401114, "quintillion", lambda: quintillion),700,5,4,10,100)
_l_(401116)