# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63325028/why-does-not-raise-typeerror-not-supported-when-all-methods-return-notimple
# Foo __eq__ and Bar __eq__ called
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
assert not _c_(461173, _n_(461172, "Foo", lambda: Foo)) == _c_(461175, _n_(461174, "Bar", lambda: Bar))
_l_(461176)

# Foo __eq__ called twice
f=_c_(461178, _n_(461177, "Foo", lambda: Foo))
_l_(461179)
assert _n_(461180, "f", lambda: f)==_n_(461181, "f", lambda: f)
_l_(461182)