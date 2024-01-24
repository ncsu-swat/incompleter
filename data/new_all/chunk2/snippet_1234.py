# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67916291/pd-dataframe-resulting-in-typeerror-when-a-metaclass-is-defined-before-it
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class MappingMeta(_n_(453673, "type", lambda: type), _a_(453676, _a_(453675, _n_(453674, "collections", lambda: collections), "abc"), "Mapping")):
    _l_(453705)

    def __setattr__(self, *args, **kwargs):
        _l_(453680)

        raise _c_(453678, _n_(453677, "RuntimeError", lambda: RuntimeError), "Can not set attributes of Mapping type")
        _l_(453679)

    def __call__(self, *args, **kwargs):
        _l_(453684)

        raise _c_(453682, _n_(453681, "RuntimeError", lambda: RuntimeError), "Can not directly instantiate Mapping type")
        _l_(453683)

    def __getitem__(self, value):
        _l_(453690)

        aux = _c_(453688, _n_(453685, "getattr", lambda: getattr), _n_(453686, "self", lambda: self), _n_(453687, "value", lambda: value))
        _l_(453689)
        return aux

    def __iter__(self):
        _l_(453699)

        aux = (_n_(453691, "k", lambda: k) for k in _c_(453694, _n_(453692, "vars", lambda: vars), _n_(453693, "self", lambda: self)) if not _c_(453697, _a_(453696, _n_(453695, "k", lambda: k), "startswith"), "_"))
        _l_(453698)
        return aux

    def __len__(self):
        _l_(453704)

        aux = _c_(453702, _n_(453700, "sum", lambda: sum), (1 for _ in _n_(453701, "self", lambda: self)))
        _l_(453703)
        return aux


class Mapping(metaclass=_n_(453706, "MappingMeta", lambda: MappingMeta)):
    _l_(453708)

    pass
    _l_(453707)


class Test(_n_(453709, "Mapping", lambda: Mapping)):
    _l_(453712)

    x = 1
    _l_(453710)
    y = 2
    _l_(453711)