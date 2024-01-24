# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57342513/function-returns-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
numberA = _c_(533951, _n_(533950, "input", lambda: input), 'Please enter a number ')
_l_(533952)

mod = _n_(533953, "numberA", lambda: numberA) % 2
_l_(533954)

if _n_(533955, "numberA", lambda: numberA) > 0:
    _l_(533962)

    _c_(533957, _n_(533956, "print", lambda: print), 'Odd')
    _l_(533958)
else:
    _c_(533960, _n_(533959, "print", lambda: print), 'Even')
    _l_(533961)