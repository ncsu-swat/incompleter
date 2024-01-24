# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67095534/forwardreference-nameerror-when-loading-a-recursive-dict-in-dataclass
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(551376, _a_(551374, _n_(551373, "marshmallow_dataclass", lambda: marshmallow_dataclass), "dataclass"), base_schema=_n_(551375, "BaseSchema", lambda: BaseSchema))
class Expression:
    _l_(551383)

    field    : _n_(551377, "str", lambda: str)
    _l_(551378)
    operator : _n_(551379, "str", lambda: str)
    _l_(551380)
    value    : _n_(551381, "str", lambda: str) 
    _l_(551382) 

@_c_(551387, _a_(551385, _n_(551384, "marshmallow_dataclass", lambda: marshmallow_dataclass), "dataclass"), base_schema=_n_(551386, "BaseSchema", lambda: BaseSchema))
class LogicalGroup:
    _l_(551394)

    group_operator   : _n_(551388, "str", lambda: str)
    _l_(551389)
    expressions      : List[Union['LogicalGroup', _n_(551390, "Expression", lambda: Expression)]] = _c_(551392, field, default_factory=_n_(551391, "list", lambda: list))
    _l_(551393)
  
@_c_(551398, _a_(551396, _n_(551395, "marshmallow_dataclass", lambda: marshmallow_dataclass), "dataclass"), base_schema=_n_(551397, "BaseSchema", lambda: BaseSchema))
class Filter:
    _l_(551403)

    rules: List[_n_(551399, "LogicalGroup", lambda: LogicalGroup)] = _c_(551401, field, default_factory=_n_(551400, "list", lambda: list))
    _l_(551402)