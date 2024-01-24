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
    _l_(702156)

except ImportError:
    pass

p = _c_(702161, _a_(702158, _n_(702157, "subprocess", lambda: subprocess), "Popen"), ["ioreg", "-rc", "AppleSmartBattery"], stdout=_a_(702160, _n_(702159, "subprocess", lambda: subprocess), "PIPE"))
_l_(702162)
output = _c_(702165, _a_(702164, _n_(702163, "p", lambda: p), "communicate"))[0]
_l_(702166)

o_max = [_n_(702167, "l", lambda: l) for l in _c_(702170, _a_(702169, _n_(702168, "output", lambda: output), "splitlines")) if 'MaxCapacity' in _n_(702171, "l", lambda: l)][0]
_l_(702172)
o_cur = [_n_(702173, "l", lambda: l) for l in _c_(702176, _a_(702175, _n_(702174, "output", lambda: output), "splitlines")) if 'CurrentCapacity' in _n_(702177, "l", lambda: l)][0]
_l_(702178)

b_max = _c_(702185, _n_(702179, "float", lambda: float), _c_(702184, _a_(702183, _c_(702182, _a_(702181, _n_(702180, "o_max", lambda: o_max), "rpartition"), '=')[-1], "strip")))
_l_(702186)
b_cur = _c_(702193, _n_(702187, "float", lambda: float), _c_(702192, _a_(702191, _c_(702190, _a_(702189, _n_(702188, "o_cur", lambda: o_cur), "rpartition"), '=')[-1], "strip")))
_l_(702194)

charge = _n_(702195, "b_cur", lambda: b_cur) / _n_(702196, "b_max", lambda: b_max)
_l_(702197)
charge_threshold = _c_(702203, _n_(702198, "int", lambda: int), _c_(702202, _a_(702200, _n_(702199, "math", lambda: math), "ceil"), 10 * _n_(702201, "charge", lambda: charge)))
_l_(702204)

# Output

total_slots, slots = 10, []
_l_(702205)
filled = _c_(702212, _n_(702206, "int", lambda: int), _c_(702211, _a_(702208, _n_(702207, "math", lambda: math), "ceil"), _n_(702209, "charge_threshold", lambda: charge_threshold) * (_n_(702210, "total_slots", lambda: total_slots) / 10.0))) * u'▸'
_l_(702213)
empty = (_n_(702214, "total_slots", lambda: total_slots) - _c_(702217, _n_(702215, "len", lambda: len), _n_(702216, "filled", lambda: filled))) * u'▹'
_l_(702218)

out = _c_(702222, _a_(702221, (_n_(702219, "filled", lambda: filled) + _n_(702220, "empty", lambda: empty)), "encode"), 'utf-8')
_l_(702223)
try:
    import sys
    _l_(702225)

except ImportError:
    pass

color_green = '%{[32m%}'
_l_(702226)
color_yellow = '%{[1;33m%}'
_l_(702227)
color_red = '%{[31m%}'
_l_(702228)
color_reset = '%{[00m%}'
_l_(702229)
color_out = (
    _n_(702230, "color_green", lambda: color_green) if _c_(702233, _n_(702231, "len", lambda: len), _n_(702232, "filled", lambda: filled)) > 6
    else _n_(702234, "color_yellow", lambda: color_yellow) if _c_(702237, _n_(702235, "len", lambda: len), _n_(702236, "filled", lambda: filled)) > 3
    else _n_(702238, "color_red", lambda: color_red)
)
_l_(702239)

out = _n_(702240, "color_out", lambda: color_out) + _n_(702241, "out", lambda: out) + _n_(702242, "color_reset", lambda: color_reset)
_l_(702243)
_c_(702248, _a_(702246, _a_(702245, _n_(702244, "sys", lambda: sys), "stdout"), "write"), _n_(702247, "out", lambda: out))
_l_(702249)