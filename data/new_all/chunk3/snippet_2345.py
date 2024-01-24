# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49614191/cx-freeze-python-3-6-typeerror-in-sklearn-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class PicklingPool(_n_(570821, "Pool", lambda: Pool)):
    _l_(570855)


    def __init__(self, processes=None, forward_reducers=None,
                 backward_reducers=None, **kwargs):
        _l_(570854)

        if _n_(570822, "forward_reducers", lambda: forward_reducers) is None:
            _l_(570826)

            forward_reducers = _c_(570824, _n_(570823, "dict", lambda: dict))
            _l_(570825)
        if _n_(570827, "backward_reducers", lambda: backward_reducers) is None:
            _l_(570831)

            backward_reducers = _c_(570829, _n_(570828, "dict", lambda: dict))
            _l_(570830)
        _n_(570832, "self", lambda: self)._forward_reducers = _n_(570833, "forward_reducers", lambda: forward_reducers)
        _l_(570834)
        _n_(570835, "self", lambda: self)._backward_reducers = _n_(570836, "backward_reducers", lambda: backward_reducers)
        _l_(570837)
        poolargs = _c_(570840, _n_(570838, "dict", lambda: dict), processes=_n_(570839, "processes", lambda: processes))
        _l_(570841)
        _c_(570845, _a_(570843, _n_(570842, "poolargs", lambda: poolargs), "update"), _n_(570844, "kwargs", lambda: kwargs))
        _l_(570846)
        _c_(570852, _a_(570850, _n_(570847, "super", lambda: super)(_n_(570848, "PicklingPool", lambda: PicklingPool), _n_(570849, "self", lambda: self)), "__init__"), **_n_(570851, "poolargs", lambda: poolargs))
        _l_(570853)