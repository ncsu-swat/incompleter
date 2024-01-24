# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/30245594/typeerror-type-str-doesnt-support-the-buffer-api
#!/usr/bin/env python
# coding=UTF-8

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import math, subprocess
    _l_(672873)

except ImportError:
    pass

p = _c_(672878, _a_(672875, _n_(672874, "subprocess", lambda: subprocess), "Popen"), ["ioreg", "-rc", "AppleSmartBattery"], stdout=_a_(672877, _n_(672876, "subprocess", lambda: subprocess), "PIPE"))
_l_(672879)
output = _c_(672882, _a_(672881, _n_(672880, "p", lambda: p), "communicate"))[0]
_l_(672883)

o_max = [_n_(672884, "l", lambda: l) for l in _c_(672887, _a_(672886, _n_(672885, "output", lambda: output), "splitlines")) if 'MaxCapacity' in _n_(672888, "l", lambda: l)][0]
_l_(672889)
o_cur = [_n_(672890, "l", lambda: l) for l in _c_(672893, _a_(672892, _n_(672891, "output", lambda: output), "splitlines")) if 'CurrentCapacity' in _n_(672894, "l", lambda: l)][0]
_l_(672895)

b_max = _c_(672902, _n_(672896, "float", lambda: float), _c_(672901, _a_(672900, _c_(672899, _a_(672898, _n_(672897, "o_max", lambda: o_max), "rpartition"), '=')[-1], "strip")))
_l_(672903)
b_cur = _c_(672910, _n_(672904, "float", lambda: float), _c_(672909, _a_(672908, _c_(672907, _a_(672906, _n_(672905, "o_cur", lambda: o_cur), "rpartition"), '=')[-1], "strip")))
_l_(672911)

charge = _n_(672912, "b_cur", lambda: b_cur) / _n_(672913, "b_max", lambda: b_max)
_l_(672914)
charge_threshold = _c_(672920, _n_(672915, "int", lambda: int), _c_(672919, _a_(672917, _n_(672916, "math", lambda: math), "ceil"), 10 * _n_(672918, "charge", lambda: charge)))
_l_(672921)

# Output

total_slots, slots = 10, []
_l_(672922)
filled = _c_(672929, _n_(672923, "int", lambda: int), _c_(672928, _a_(672925, _n_(672924, "math", lambda: math), "ceil"), _n_(672926, "charge_threshold", lambda: charge_threshold) * (_n_(672927, "total_slots", lambda: total_slots) / 10.0))) * u'▸'
_l_(672930)
empty = (_n_(672931, "total_slots", lambda: total_slots) - _c_(672934, _n_(672932, "len", lambda: len), _n_(672933, "filled", lambda: filled))) * u'▹'
_l_(672935)

out = _c_(672939, _a_(672938, (_n_(672936, "filled", lambda: filled) + _n_(672937, "empty", lambda: empty)), "encode"), 'utf-8')
_l_(672940)
try:
    import sys
    _l_(672942)

except ImportError:
    pass

color_green = '%{[32m%}'
_l_(672943)
color_yellow = '%{[1;33m%}'
_l_(672944)
color_red = '%{[31m%}'
_l_(672945)
color_reset = '%{[00m%}'
_l_(672946)
color_out = (
    _n_(672947, "color_green", lambda: color_green) if _c_(672950, _n_(672948, "len", lambda: len), _n_(672949, "filled", lambda: filled)) > 6
    else _n_(672951, "color_yellow", lambda: color_yellow) if _c_(672954, _n_(672952, "len", lambda: len), _n_(672953, "filled", lambda: filled)) > 3
    else _n_(672955, "color_red", lambda: color_red)
)
_l_(672956)

out = _n_(672957, "color_out", lambda: color_out) + _n_(672958, "out", lambda: out) + _n_(672959, "color_reset", lambda: color_reset)
_l_(672960)
_c_(672965, _a_(672963, _a_(672962, _n_(672961, "sys", lambda: sys), "stdout"), "write"), _n_(672964, "out", lambda: out))
_l_(672966)