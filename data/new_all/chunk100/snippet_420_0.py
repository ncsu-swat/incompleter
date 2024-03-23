# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def is_samePatterns(colors, patterns):
    _l_(41326)

    if _c_(41249, _n_(41247, "len", lambda: len), _n_(41248, "colors", lambda: colors)) != _c_(41252, _n_(41250, "len", lambda: len), _n_(41251, "patterns", lambda: patterns)):
        _l_(41254)

        aux = False
        _l_(41253)
        return aux
    sdict = {}
    _l_(41255)
    pset = _c_(41257, _n_(41256, "set", lambda: set))
    _l_(41258)
    sset = _c_(41260, _n_(41259, "set", lambda: set))
    _l_(41261)
    for i in _c_(41266, _n_(41262, "range", lambda: range), _c_(41265, _n_(41263, "len", lambda: len), _n_(41264, "patterns", lambda: patterns))):
        _l_(41300)

        _c_(41271, _a_(41268, _n_(41267, "pset", lambda: pset), "add"), _n_(41269, "patterns", lambda: patterns)[_n_(41270, "i", lambda: i)])
        _l_(41272)
        _c_(41277, _a_(41274, _n_(41273, "sset", lambda: sset), "add"), _n_(41275, "colors", lambda: colors)[_n_(41276, "i", lambda: i)])
        _l_(41278)
        if _n_(41279, "patterns", lambda: patterns)[_n_(41280, "i", lambda: i)] not in _c_(41283, _a_(41282, _n_(41281, "sdict", lambda: sdict), "keys")):
            _l_(41288)

            _n_(41284, "sdict", lambda: sdict)[_n_(41285, "patterns", lambda: patterns)[_n_(41286, "i", lambda: i)]] = []
            _l_(41287)
        _c_(41293, _a_(41290, _n_(41289, "keys", lambda: keys), "append"), _n_(41291, "colors", lambda: colors)[_n_(41292, "i", lambda: i)])
        _l_(41294)
        _n_(41295, "sdict", lambda: sdict)[_n_(41296, "patterns", lambda: patterns)[_n_(41297, "i", lambda: i)]] = _n_(41298, "keys", lambda: keys)
        _l_(41299)
    if _c_(41303, _n_(41301, "len", lambda: len), _n_(41302, "pset", lambda: pset)) != _c_(41306, _n_(41304, "len", lambda: len), _n_(41305, "sset", lambda: sset)):
        _l_(41308)

        aux = False
        _l_(41307)
        return aux
    for values in _c_(41311, _a_(41310, _n_(41309, "sdict", lambda: sdict), "values")):
        _l_(41324)

        for i in _c_(41316, _n_(41312, "range", lambda: range), _c_(41315, _n_(41313, "len", lambda: len), _n_(41314, "values", lambda: values)) - 1):
            _l_(41323)

            if _n_(41317, "values", lambda: values)[_n_(41318, "i", lambda: i)] != _n_(41319, "values", lambda: values)[_n_(41320, "i", lambda: i) + 1]:
                _l_(41322)

                aux = False
                _l_(41321)
                return aux
    aux = True
    _l_(41325)
    return aux
_c_(41330, _n_(41327, "print", lambda: print), _c_(41329, _n_(41328, "is_samePatterns", lambda: is_samePatterns), ['red', 'green', 'green'], ['a', 'b', 'b']))
_l_(41331)
_c_(41335, _n_(41332, "print", lambda: print), _c_(41334, _n_(41333, "is_samePatterns", lambda: is_samePatterns), ['red', 'green', 'greenn'], ['a', 'b', 'b']))
_l_(41336)