# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def is_samePatterns(colors, patterns):
    _l_(41601)

    if _c_(41523, _n_(41521, "len", lambda: len), _n_(41522, "colors", lambda: colors)) != _c_(41526, _n_(41524, "len", lambda: len), _n_(41525, "patterns", lambda: patterns)):
        _l_(41528)

        aux = False
        _l_(41527)
        return aux
    sdict = {}
    _l_(41529)
    pset = _c_(41531, _n_(41530, "set", lambda: set))
    _l_(41532)
    for i in _c_(41537, _n_(41533, "range", lambda: range), _c_(41536, _n_(41534, "len", lambda: len), _n_(41535, "patterns", lambda: patterns))):
        _l_(41575)

        _c_(41542, _a_(41539, _n_(41538, "pset", lambda: pset), "add"), _n_(41540, "patterns", lambda: patterns)[_n_(41541, "i", lambda: i)])
        _l_(41543)
        _c_(41548, _a_(41545, _n_(41544, "sset", lambda: sset), "add"), _n_(41546, "colors", lambda: colors)[_n_(41547, "i", lambda: i)])
        _l_(41549)
        if _n_(41550, "patterns", lambda: patterns)[_n_(41551, "i", lambda: i)] not in _c_(41554, _a_(41553, _n_(41552, "sdict", lambda: sdict), "keys")):
            _l_(41559)

            _n_(41555, "sdict", lambda: sdict)[_n_(41556, "patterns", lambda: patterns)[_n_(41557, "i", lambda: i)]] = []
            _l_(41558)
        keys = _n_(41560, "sdict", lambda: sdict)[_n_(41561, "patterns", lambda: patterns)[_n_(41562, "i", lambda: i)]]
        _l_(41563)
        _c_(41568, _a_(41565, _n_(41564, "keys", lambda: keys), "append"), _n_(41566, "colors", lambda: colors)[_n_(41567, "i", lambda: i)])
        _l_(41569)
        _n_(41570, "sdict", lambda: sdict)[_n_(41571, "patterns", lambda: patterns)[_n_(41572, "i", lambda: i)]] = _n_(41573, "keys", lambda: keys)
        _l_(41574)
    if _c_(41578, _n_(41576, "len", lambda: len), _n_(41577, "pset", lambda: pset)) != _c_(41581, _n_(41579, "len", lambda: len), _n_(41580, "sset", lambda: sset)):
        _l_(41583)

        aux = False
        _l_(41582)
        return aux
    for values in _c_(41586, _a_(41585, _n_(41584, "sdict", lambda: sdict), "values")):
        _l_(41599)

        for i in _c_(41591, _n_(41587, "range", lambda: range), _c_(41590, _n_(41588, "len", lambda: len), _n_(41589, "values", lambda: values)) - 1):
            _l_(41598)

            if _n_(41592, "values", lambda: values)[_n_(41593, "i", lambda: i)] != _n_(41594, "values", lambda: values)[_n_(41595, "i", lambda: i) + 1]:
                _l_(41597)

                aux = False
                _l_(41596)
                return aux
    aux = True
    _l_(41600)
    return aux
_c_(41605, _n_(41602, "print", lambda: print), _c_(41604, _n_(41603, "is_samePatterns", lambda: is_samePatterns), ['red', 'green', 'green'], ['a', 'b', 'b']))
_l_(41606)
_c_(41610, _n_(41607, "print", lambda: print), _c_(41609, _n_(41608, "is_samePatterns", lambda: is_samePatterns), ['red', 'green', 'greenn'], ['a', 'b', 'b']))
_l_(41611)