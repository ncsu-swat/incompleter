# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
xs = [8, 23, 45]
_l_(1547905)
for i in _c_(1547910, _n_(1547906, "range", lambda: range), _c_(1547909, _n_(1547907, "len", lambda: len), _n_(1547908, "xs", lambda: xs))):
    _l_(1547919)

    _c_(1547917, _n_(1547911, "print", lambda: print), _c_(1547916, _a_(1547912, "item #{} = {}", "format"), _n_(1547913, "i", lambda: i) + 1, _n_(1547914, "xs", lambda: xs)[_n_(1547915, "i", lambda: i)]))
    _l_(1547918)

xs = [8, 23, 45]
_l_(1547920)
for idx, val in _c_(1547923, _n_(1547921, "enumerate", lambda: enumerate), _n_(1547922, "xs", lambda: xs), start=1):
    _l_(1547931)

    _c_(1547929, _n_(1547924, "print", lambda: print), _c_(1547928, _a_(1547925, "item #{} = {}", "format"), _n_(1547926, "idx", lambda: idx), _n_(1547927, "val", lambda: val)))
    _l_(1547930)

