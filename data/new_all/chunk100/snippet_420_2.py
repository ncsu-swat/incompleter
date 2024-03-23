# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def is_samePatterns(colors, patterns):
    _l_(41510)

    if _c_(41430, _n_(41428, "len", lambda: len), _n_(41429, "colors", lambda: colors)) != _c_(41433, _n_(41431, "len", lambda: len), _n_(41432, "patterns", lambda: patterns)):
        _l_(41435)

        aux = False
        _l_(41434)
        return aux
    pset = _c_(41437, _n_(41436, "set", lambda: set))
    _l_(41438)
    sset = _c_(41440, _n_(41439, "set", lambda: set))
    _l_(41441)
    for i in _c_(41446, _n_(41442, "range", lambda: range), _c_(41445, _n_(41443, "len", lambda: len), _n_(41444, "patterns", lambda: patterns))):
        _l_(41484)

        _c_(41451, _a_(41448, _n_(41447, "pset", lambda: pset), "add"), _n_(41449, "patterns", lambda: patterns)[_n_(41450, "i", lambda: i)])
        _l_(41452)
        _c_(41457, _a_(41454, _n_(41453, "sset", lambda: sset), "add"), _n_(41455, "colors", lambda: colors)[_n_(41456, "i", lambda: i)])
        _l_(41458)
        if _n_(41459, "patterns", lambda: patterns)[_n_(41460, "i", lambda: i)] not in _c_(41463, _a_(41462, _n_(41461, "sdict", lambda: sdict), "keys")):
            _l_(41468)

            _n_(41464, "sdict", lambda: sdict)[_n_(41465, "patterns", lambda: patterns)[_n_(41466, "i", lambda: i)]] = []
            _l_(41467)
        keys = _n_(41469, "sdict", lambda: sdict)[_n_(41470, "patterns", lambda: patterns)[_n_(41471, "i", lambda: i)]]
        _l_(41472)
        _c_(41477, _a_(41474, _n_(41473, "keys", lambda: keys), "append"), _n_(41475, "colors", lambda: colors)[_n_(41476, "i", lambda: i)])
        _l_(41478)
        _n_(41479, "sdict", lambda: sdict)[_n_(41480, "patterns", lambda: patterns)[_n_(41481, "i", lambda: i)]] = _n_(41482, "keys", lambda: keys)
        _l_(41483)
    if _c_(41487, _n_(41485, "len", lambda: len), _n_(41486, "pset", lambda: pset)) != _c_(41490, _n_(41488, "len", lambda: len), _n_(41489, "sset", lambda: sset)):
        _l_(41492)

        aux = False
        _l_(41491)
        return aux
    for values in _c_(41495, _a_(41494, _n_(41493, "sdict", lambda: sdict), "values")):
        _l_(41508)

        for i in _c_(41500, _n_(41496, "range", lambda: range), _c_(41499, _n_(41497, "len", lambda: len), _n_(41498, "values", lambda: values)) - 1):
            _l_(41507)

            if _n_(41501, "values", lambda: values)[_n_(41502, "i", lambda: i)] != _n_(41503, "values", lambda: values)[_n_(41504, "i", lambda: i) + 1]:
                _l_(41506)

                aux = False
                _l_(41505)
                return aux
    aux = True
    _l_(41509)
    return aux
_c_(41514, _n_(41511, "print", lambda: print), _c_(41513, _n_(41512, "is_samePatterns", lambda: is_samePatterns), ['red', 'green', 'green'], ['a', 'b', 'b']))
_l_(41515)
_c_(41519, _n_(41516, "print", lambda: print), _c_(41518, _n_(41517, "is_samePatterns", lambda: is_samePatterns), ['red', 'green', 'greenn'], ['a', 'b', 'b']))
_l_(41520)