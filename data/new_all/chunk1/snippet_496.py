# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/33586052/typeerror-unorderable-types-int-list
# Import Packages
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(390061)

except ImportError:
    pass

# Global Variables
perf_num = 500
_l_(390062)
species = [20]
_l_(390063)
temp_num = 0
_l_(390064)
length = 0
_l_(390065)
s = 0
_l_(390066)

# Main Program
for num in _c_(390068, _n_(390067, "range", lambda: range), 100):
    _l_(390128)

    r1 = _c_(390073, _n_(390069, "int", lambda: int), _c_(390072, _a_(390071, _n_(390070, "random", lambda: random), "random"))*10)
    _l_(390074)
    r2 = _c_(390079, _n_(390075, "int", lambda: int), _c_(390078, _a_(390077, _n_(390076, "random", lambda: random), "random"))*10)
    _l_(390080)
    _c_(390084, _a_(390082, _n_(390081, "species", lambda: species), "append"), _n_(390083, "r1", lambda: r1))
    _l_(390085)
    length = _c_(390088, _n_(390086, "len", lambda: len), _n_(390087, "species", lambda: species))
    _l_(390089)
    while _n_(390090, "s", lambda: s) < _n_(390091, "length", lambda: length):
        _l_(390123)

        _c_(390094, _n_(390092, "print", lambda: print), _n_(390093, "s", lambda: s))
        _l_(390095)
        if _n_(390096, "species", lambda: species)[_n_(390097, "s", lambda: s)-1] > _n_(390098, "species", lambda: species)[_n_(390099, "s", lambda: s)]:
            _l_(390116)

            temp_num = _n_(390100, "species", lambda: species)[_n_(390101, "s", lambda: s)-1] - _n_(390102, "r1", lambda: r1)
            _l_(390103)
            _n_(390104, "species", lambda: species)[_n_(390105, "s", lambda: s)-1] = _n_(390106, "temp_num", lambda: temp_num)
            _l_(390107)
        else:
            temp_num = _n_(390108, "species", lambda: species)[_n_(390109, "s", lambda: s)] - _n_(390110, "r1", lambda: r1)
            _l_(390111)
            _n_(390112, "species", lambda: species)[_n_(390113, "s", lambda: s)] = _n_(390114, "temp_num", lambda: temp_num)
            _l_(390115)
        if _n_(390117, "s", lambda: s)-1 < 5:
            _l_(390121)

            _n_(390118, "species", lambda: species)[_n_(390119, "s", lambda: s)-1] = []
            _l_(390120)
        s += 1
        _l_(390122)

    _c_(390126, _n_(390124, "print", lambda: print), _n_(390125, "species", lambda: species))
    _l_(390127)