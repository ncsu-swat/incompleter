# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55401633/how-to-avoid-a-nameerror-when-making-an-alias-to-annotation-type-using-circular
from __future__ import annotations
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_l_(399968)
try:
    import typing
    _l_(399970)

except ImportError:
    pass

MyType1 = _a_(399972, _n_(399971, "typing", lambda: typing), "Union")[_n_(399973, "str", lambda: str), _n_(399974, "MyType2", lambda: MyType2)]
_l_(399975)
MyType2 = _a_(399977, _n_(399976, "typing", lambda: typing), "Mapping")[_n_(399978, "str", lambda: str), _n_(399979, "MyType1", lambda: MyType1)]
_l_(399980)