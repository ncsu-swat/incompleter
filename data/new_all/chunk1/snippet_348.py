# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64641718/python-caching-typeerror-unhashable-type-dict
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def memoize(func):
    _l_(401377)

    """Store the results of the decorated function for fast lookup
    """

    # Store results in a dict that maps arguments to results
    cache = {}
    _l_(401357)

    def wrapper(*args, **kwargs):
        _l_(401374)

        # If these arguments haven't been seen before, call func() and store the result.
        if (_n_(401358, "args", lambda: args), _n_(401359, "kwargs", lambda: kwargs)) not in _n_(401360, "cache", lambda: cache):
            _l_(401369)

            _n_(401361, "cache", lambda: cache)[(_n_(401362, "args", lambda: args), _n_(401363, "kwargs", lambda: kwargs))] = _c_(401367, _n_(401364, "func", lambda: func), *_n_(401365, "args", lambda: args), **_n_(401366, "kwargs", lambda: kwargs))          
            _l_(401368)          
        aux = _n_(401370, "cache", lambda: cache)[(_n_(401371, "args", lambda: args), _n_(401372, "kwargs", lambda: kwargs))]
        _l_(401373)
        return aux
    aux = _n_(401375, "wrapper", lambda: wrapper)
    _l_(401376)

    return aux

@_n_(401378, "memoize", lambda: memoize)
def add(a, b):
    _l_(401385)

    _c_(401380, _n_(401379, "print", lambda: print), 'Sleeping...')
    _l_(401381)
    aux = _n_(401382, "a", lambda: a) + _n_(401383, "b", lambda: b)
    _l_(401384)
    return aux

_c_(401387, _n_(401386, "add", lambda: add), 1, 2)
_l_(401388)