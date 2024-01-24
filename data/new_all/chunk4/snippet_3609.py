# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71358734/attributeerror-module-dataclasses-has-no-attribute-is-dataclass
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pydantic import BaseModel, create_model
    _l_(612007)

except ImportError:
    pass
MyModel = _c_(612009, _n_(612008, "create_model", lambda: create_model), 'MyModel', foo="foo")
_l_(612010)