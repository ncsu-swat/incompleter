# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59822759/python-import-random-issue-attributeerror-builtin-function-or-method-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
characters = _a_(700953, _n_(700952, "string", lambda: string), "ascii_letters") + _a_(700955, _n_(700954, "string", lambda: string), "digits")
_l_(700956)
passwordGen =  _c_(700965, _a_(700957, "", "join"), (_c_(700960, _n_(700958, "choice", lambda: choice), _n_(700959, "characters", lambda: characters)) for x in _c_(700964, _n_(700961, "range", lambda: range), _c_(700963, _n_(700962, "randint", lambda: randint), 12, 20))))
_l_(700966)