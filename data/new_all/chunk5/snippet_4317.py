# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59822759/python-import-random-issue-attributeerror-builtin-function-or-method-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
characters = _a_(648414, _n_(648413, "string", lambda: string), "ascii_letters") + _a_(648416, _n_(648415, "string", lambda: string), "digits")
_l_(648417)
passwordGen =  _c_(648426, _a_(648418, "", "join"), (_c_(648421, _n_(648419, "choice", lambda: choice), _n_(648420, "characters", lambda: characters)) for x in _c_(648425, _n_(648422, "range", lambda: range), _c_(648424, _n_(648423, "randint", lambda: randint), 12, 20))))
_l_(648427)