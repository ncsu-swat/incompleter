# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67095534/forwardreference-nameerror-when-loading-a-recursive-dict-in-dataclass
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(449514, _a_(449512, _n_(449511, "marshmallow_dataclass", lambda: marshmallow_dataclass), "dataclass"), base_schema=_n_(449513, "BaseSchema", lambda: BaseSchema))
class Expression:
    _l_(449521)

    field    : _n_(449515, "str", lambda: str)
    _l_(449516)
    operator : _n_(449517, "str", lambda: str)
    _l_(449518)
    value    : _n_(449519, "str", lambda: str) 
    _l_(449520) 

@_c_(449525, _a_(449523, _n_(449522, "marshmallow_dataclass", lambda: marshmallow_dataclass), "dataclass"), base_schema=_n_(449524, "BaseSchema", lambda: BaseSchema))
class LogicalGroup:
    _l_(449532)

    group_operator   : _n_(449526, "str", lambda: str)
    _l_(449527)
    expressions      : List[Union['LogicalGroup', _n_(449528, "Expression", lambda: Expression)]] = _c_(449530, field, default_factory=_n_(449529, "list", lambda: list))
    _l_(449531)
  
@_c_(449536, _a_(449534, _n_(449533, "marshmallow_dataclass", lambda: marshmallow_dataclass), "dataclass"), base_schema=_n_(449535, "BaseSchema", lambda: BaseSchema))
class Filter:
    _l_(449541)

    rules: List[_n_(449537, "LogicalGroup", lambda: LogicalGroup)] = _c_(449539, field, default_factory=_n_(449538, "list", lambda: list))
    _l_(449540)