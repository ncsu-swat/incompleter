# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/772124/what-does-the-ellipsis-object-do
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Foo:
    _l_(62318)

    bar: Any = ...
    _l_(62315)
    def __init__(self, name: _n_(62316, "str", lambda: str)=...) -> None:
        _l_(62317)

...
