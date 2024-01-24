# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49566391/nameerror-for-importing-random-and-numpy-random-but-nothing-else
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
rounds = 10
_l_(528507)
probability = 100
_l_(528508)
items = [1, 2, 3, 4, 5]
_l_(528509)
for r in _c_(528512, _n_(528510, "range", lambda: range), 1, _n_(528511, "rounds", lambda: rounds)):
    _l_(528521)

    try:
        from numpy.random import uniform
        _l_(528514)

    except ImportError:
        pass
    sample = {_n_(528515, "item", lambda: item): _c_(528517, _n_(528516, "uniform", lambda: uniform)) < _n_(528518, "probability", lambda: probability) for item in _n_(528519, "items", lambda: items)}
    _l_(528520)