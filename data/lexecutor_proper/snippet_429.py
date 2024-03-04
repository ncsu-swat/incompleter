# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/773/how-do-i-use-itertools-groupby
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for x in _c_(62919, _n_(62914, "list", lambda: list), _c_(62918, _n_(62915, "groupby", lambda: groupby), _c_(62917, _n_(62916, "range", lambda: range), 10))):
    _l_(62926)

    _c_(62924, _n_(62920, "print", lambda: print), _c_(62923, _n_(62921, "list", lambda: list), _n_(62922, "x", lambda: x)[1]))
    _l_(62925)

[]
_l_(62927)
[]
_l_(62928)
[]
_l_(62929)
[]
_l_(62930)
[]
_l_(62931)
[]
_l_(62932)
[]
_l_(62933)
[]
_l_(62934)
[]
_l_(62935)
[9]
_l_(62936)

def groupbylist(*args, **kwargs):
    _l_(62946)

    aux = [(_n_(62937, "k", lambda: k), _c_(62940, _n_(62938, "list", lambda: list), _n_(62939, "g", lambda: g))) for k, g in _c_(62944, _n_(62941, "groupby", lambda: groupby), *_n_(62942, "args", lambda: args), **_n_(62943, "kwargs", lambda: kwargs))]
    _l_(62945)
    return aux

