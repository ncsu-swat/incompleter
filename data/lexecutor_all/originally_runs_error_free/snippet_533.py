# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4211209/remove-all-the-elements-that-occur-in-one-list-from-another
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(1545929, _a_(1545928, _c_(1545927, _n_(1545926, "set", lambda: set), [1,2,6,8]), "difference"), [2,3,5,8])
_l_(1545930)
{1, 6}
_l_(1545931)

l1, l2 = [1,2,6,8], [2,3,5,8]
_l_(1545932)
s2 = _c_(1545935, _n_(1545933, "set", lambda: set), _n_(1545934, "l2", lambda: l2))  # Type-cast `l2` to `set`
_l_(1545936)  # Type-cast `l2` to `set`

l3 = [_n_(1545937, "x", lambda: x) for x in _n_(1545938, "l1", lambda: l1) if _n_(1545939, "x", lambda: x) not in _n_(1545940, "s2", lambda: s2)]
_l_(1545941)
                             #   ^ Doing membership checking on `set` s2

l1 = [1,2,6,8]
_l_(1545942)
l2 = _c_(1545944, _n_(1545943, "set", lambda: set), [2,3,5,8])
_l_(1545945)

#     v  `filter` returns the a iterator object. Here I'm type-casting 
#     v  it to `list` in order to display the resultant value
_c_(1545952, _n_(1545946, "list", lambda: list), _c_(1545951, _n_(1545947, "filter", lambda: filter), lambda x: _n_(1545948, "x", lambda: x) not in _n_(1545949, "l2", lambda: l2), _n_(1545950, "l1", lambda: l1)))
_l_(1545953)
[1, 6]
_l_(1545954)

