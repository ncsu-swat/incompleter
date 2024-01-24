# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46502885/why-does-using-super-in-a-call-method-on-a-metaclass-raise-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class ListMetaclass(_n_(381688, "type", lambda: type)):
    _l_(381733)

    def __new__(cls, name, bases, attrs):
        _l_(381705)

        _n_(381689, "attrs", lambda: attrs)['add'] = lambda self, value: _c_(381693, _a_(381691, _n_(381690, "self", lambda: self), "append"), _n_(381692, "value", lambda: value))
        _l_(381694)
        new_cls = _c_(381701, _a_(381696, _n_(381695, "type", lambda: type), "__new__"), _n_(381697, "cls", lambda: cls), _n_(381698, "name", lambda: name), _n_(381699, "bases", lambda: bases), _n_(381700, "attrs", lambda: attrs))
        _l_(381702)
        aux = _n_(381703, "new_cls", lambda: new_cls)
        _l_(381704)
        return aux

    def __call__(cls, *args, **kw):
        _l_(381732)

        aux = _c_(381711, _a_(381707, _n_(381706, "super", lambda: super)(), "__call__"), _n_(381708, "cls", lambda: cls), *_n_(381709, "args", lambda: args), **_n_(381710, "kw", lambda: kw))
        _l_(381712)
        ### why the 'super()' here raises TypeError: 'ListMetaclass' object is not iterable
        return aux
        aux = _c_(381720, _a_(381716, _n_(381713, "super", lambda: super)(_n_(381714, "__class__", lambda: __class__), _n_(381715, "cls", lambda: cls)), "__call__"), _n_(381717, "cls", lambda: cls), *_n_(381718, "args", lambda: args), **_n_(381719, "kw", lambda: kw))
        _l_(381721)
        return aux
        aux = _c_(381730, _a_(381726, _n_(381722, "super", lambda: super)(_n_(381723, "__class__", lambda: __class__), _a_(381725, _n_(381724, "cls", lambda: cls), "__class__")), "__call__"), _n_(381727, "cls", lambda: cls), *_n_(381728, "args", lambda: args), **_n_(381729, "kw", lambda: kw))
        _l_(381731)
        return aux

class MyList(_n_(381734, "list", lambda: list), metaclass=_n_(381735, "ListMetaclass", lambda: ListMetaclass)):
    _l_(381741)

    a=1
    _l_(381736)
    def bar(self):
        _l_(381740)

        _c_(381738, _n_(381737, "print", lambda: print), 'test');
        _l_(381739)

L=_c_(381743, _n_(381742, "MyList", lambda: MyList))
_l_(381744)
_c_(381747, _a_(381746, _n_(381745, "L", lambda: L), "add"), 1)
_l_(381748)
_c_(381751, _n_(381749, "print", lambda: print), 'Print MyList :', _n_(381750, "L", lambda: L))
_l_(381752)