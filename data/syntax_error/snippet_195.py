# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/54867/what-is-the-difference-between-old-style-and-new-style-classes-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class C:
    _l_(1546352)

i = 0class C1(_n_(1546353, "C", lambda: C)):
    _l_(1546354)

passclass C2(_n_(1546355, "C", lambda: C)):
    _l_(1546356)

i = 2class C12(_n_(1546357, "C1", lambda: C1), _n_(1546358, "C2", lambda: C2)):
    _l_(1546359)

passclass C21(_n_(1546360, "C2", lambda: C2), _n_(1546361, "C1", lambda: C1)):
    _l_(1546362)

pass
assert _a_(1546365, _c_(1546364, _n_(1546363, "C12", lambda: C12)), "i") == 0
_l_(1546366)
assert _a_(1546369, _c_(1546368, _n_(1546367, "C21", lambda: C21)), "i") == 2
_l_(1546370)

try:
    _l_(1546378)

    _a_(1546372, _n_(1546371, "C12", lambda: C12), "__mro__")
    _l_(1546373)
except _n_(1546374, "AttributeError", lambda: AttributeError):
    _l_(1546376)

    pass
    _l_(1546375)
else:
    assert False
    _l_(1546377)

class C(_n_(1546379, "object", lambda: object)):
    _l_(1546380)

i = 0class C1(_n_(1546381, "C", lambda: C)):
    _l_(1546382)

passclass C2(_n_(1546383, "C", lambda: C)):
    _l_(1546384)

i = 2class C12(_n_(1546385, "C1", lambda: C1), _n_(1546386, "C2", lambda: C2)):
    _l_(1546387)

passclass C21(_n_(1546388, "C2", lambda: C2), _n_(1546389, "C1", lambda: C1)):
    _l_(1546390)

pass
assert _a_(1546393, _c_(1546392, _n_(1546391, "C12", lambda: C12)), "i") == 2
_l_(1546394)
assert _a_(1546397, _c_(1546396, _n_(1546395, "C21", lambda: C21)), "i") == 2
_l_(1546398)

assert _a_(1546400, _n_(1546399, "C12", lambda: C12), "__mro__") == (_n_(1546401, "C12", lambda: C12), _n_(1546402, "C1", lambda: C1), _n_(1546403, "C2", lambda: C2), _n_(1546404, "C", lambda: C), _n_(1546405, "object", lambda: object))
_l_(1546406)
assert _a_(1546408, _n_(1546407, "C21", lambda: C21), "__mro__") == (_n_(1546409, "C21", lambda: C21), _n_(1546410, "C2", lambda: C2), _n_(1546411, "C1", lambda: C1), _n_(1546412, "C", lambda: C), _n_(1546413, "object", lambda: object))
_l_(1546414)

# OK, old:
class Old:
    _l_(1546415)

passtry:
    _l_(1546423)

    raise _c_(1546417, _n_(1546416, "Old", lambda: Old))
    _l_(1546418)
except _n_(1546419, "Old", lambda: Old):
    _l_(1546421)

    pass
    _l_(1546420)
else:
    assert False
    _l_(1546422)

# TypeError, new not derived from `Exception`.
class New(_n_(1546424, "object", lambda: object)):
    _l_(1546425)

passtry:
    _l_(1546433)

    raise _c_(1546427, _n_(1546426, "New", lambda: New))
    _l_(1546428)
except _n_(1546429, "TypeError", lambda: TypeError):
    _l_(1546431)

    pass
    _l_(1546430)
else:
    assert False
    _l_(1546432)

# OK, derived from `Exception`.
class New(_n_(1546434, "Exception", lambda: Exception)):
    _l_(1546435)

passtry:
    _l_(1546443)

    raise _c_(1546437, _n_(1546436, "New", lambda: New))
    _l_(1546438)
except _n_(1546439, "New", lambda: New):
    _l_(1546441)

    pass
    _l_(1546440)
else:
    assert False
    _l_(1546442)

# `'str'` is a new style object, so you can't raise it:
try:
    _l_(1546449)

    raise 'str'
    _l_(1546444)
except _n_(1546445, "TypeError", lambda: TypeError):
    _l_(1546447)

    pass
    _l_(1546446)
else:
    assert False
    _l_(1546448)

