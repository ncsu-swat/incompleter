# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63729685/how-to-differentiate-between-unexpected-keyword-argument-and-missing-positional
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    _l_(432963)

    _c_(432947, _n_(432946, "test_method", lambda: test_method))
    _l_(432948)
except _c_(432951, _n_(432949, "TypeError", lambda: TypeError), _n_(432950, "MissingPositionalArgument", lambda: MissingPositionalArgument)):
    _l_(432955)

    _c_(432953, _n_(432952, "do_something", lambda: do_something))
    _l_(432954)
except _c_(432958, _n_(432956, "TypeError", lambda: TypeError), _n_(432957, "UnexpectedKeywordArgument", lambda: UnexpectedKeywordArgument)):
    _l_(432962)

    _c_(432960, _n_(432959, "do_something_else", lambda: do_something_else))
    _l_(432961)