# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def is_samePatterns(colors, patterns):
    _l_(41417)

    if _c_(41339, _n_(41337, "len", lambda: len), _n_(41338, "colors", lambda: colors)) != _c_(41342, _n_(41340, "len", lambda: len), _n_(41341, "patterns", lambda: patterns)):
        _l_(41344)

        aux = False
        _l_(41343)
        return aux
    sdict = {}
    _l_(41345)
    sset = _c_(41347, _n_(41346, "set", lambda: set))
    _l_(41348)
    for i in _c_(41353, _n_(41349, "range", lambda: range), _c_(41352, _n_(41350, "len", lambda: len), _n_(41351, "patterns", lambda: patterns))):
        _l_(41391)

        _c_(41358, _a_(41355, _n_(41354, "pset", lambda: pset), "add"), _n_(41356, "patterns", lambda: patterns)[_n_(41357, "i", lambda: i)])
        _l_(41359)
        _c_(41364, _a_(41361, _n_(41360, "sset", lambda: sset), "add"), _n_(41362, "colors", lambda: colors)[_n_(41363, "i", lambda: i)])
        _l_(41365)
        if _n_(41366, "patterns", lambda: patterns)[_n_(41367, "i", lambda: i)] not in _c_(41370, _a_(41369, _n_(41368, "sdict", lambda: sdict), "keys")):
            _l_(41375)

            _n_(41371, "sdict", lambda: sdict)[_n_(41372, "patterns", lambda: patterns)[_n_(41373, "i", lambda: i)]] = []
            _l_(41374)
        keys = _n_(41376, "sdict", lambda: sdict)[_n_(41377, "patterns", lambda: patterns)[_n_(41378, "i", lambda: i)]]
        _l_(41379)
        _c_(41384, _a_(41381, _n_(41380, "keys", lambda: keys), "append"), _n_(41382, "colors", lambda: colors)[_n_(41383, "i", lambda: i)])
        _l_(41385)
        _n_(41386, "sdict", lambda: sdict)[_n_(41387, "patterns", lambda: patterns)[_n_(41388, "i", lambda: i)]] = _n_(41389, "keys", lambda: keys)
        _l_(41390)
    if _c_(41394, _n_(41392, "len", lambda: len), _n_(41393, "pset", lambda: pset)) != _c_(41397, _n_(41395, "len", lambda: len), _n_(41396, "sset", lambda: sset)):
        _l_(41399)

        aux = False
        _l_(41398)
        return aux
    for values in _c_(41402, _a_(41401, _n_(41400, "sdict", lambda: sdict), "values")):
        _l_(41415)

        for i in _c_(41407, _n_(41403, "range", lambda: range), _c_(41406, _n_(41404, "len", lambda: len), _n_(41405, "values", lambda: values)) - 1):
            _l_(41414)

            if _n_(41408, "values", lambda: values)[_n_(41409, "i", lambda: i)] != _n_(41410, "values", lambda: values)[_n_(41411, "i", lambda: i) + 1]:
                _l_(41413)

                aux = False
                _l_(41412)
                return aux
    aux = True
    _l_(41416)
    return aux
_c_(41421, _n_(41418, "print", lambda: print), _c_(41420, _n_(41419, "is_samePatterns", lambda: is_samePatterns), ['red', 'green', 'green'], ['a', 'b', 'b']))
_l_(41422)
_c_(41426, _n_(41423, "print", lambda: print), _c_(41425, _n_(41424, "is_samePatterns", lambda: is_samePatterns), ['red', 'green', 'greenn'], ['a', 'b', 'b']))
_l_(41427)