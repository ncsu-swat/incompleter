# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/15112125/how-to-test-multiple-variables-for-equality-against-a-single-value
# ✅ test multiple variables against single value using tuple

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if 'a' in (_n_(62294, "a", lambda: a), _n_(62295, "b", lambda: b), _n_(62296, "c", lambda: c)):
    _l_(62300)

    _c_(62298, _n_(62297, "print", lambda: print), 'value is stored in at least one of the variables')
    _l_(62299)

# ---------------------------------------------------------

# ✅ test multiple variables against single value using tuple

if 'a' in {_n_(62301, "a", lambda: a), _n_(62302, "b", lambda: b), _n_(62303, "c", lambda: c)}:
    _l_(62307)

    _c_(62305, _n_(62304, "print", lambda: print), 'value is stored in at least one of the variables')
    _l_(62306)

# ---------------------------------------------------------


# ✅ test multiple variables against single value (OR operator chaining)
if _n_(62308, "a", lambda: a) == 'a' or _n_(62309, "b", lambda: b) == 'a' or _n_(62310, "c", lambda: c) == 'a':
    _l_(62314)

    _c_(62312, _n_(62311, "print", lambda: print), 'value is stored in at least one of the variables')
    _l_(62313)

