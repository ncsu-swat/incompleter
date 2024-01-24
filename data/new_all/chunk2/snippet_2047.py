# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67095534/forwardreference-nameerror-when-loading-a-recursive-dict-in-dataclass
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import marshmallow_dataclass
    _l_(472613)

except ImportError:
    pass
try:
    from dataclasses import field
    _l_(472615)

except ImportError:
    pass
try:
    from api_handler import BaseSchema
    _l_(472617)

except ImportError:
    pass
try:
    from typing import Sequence, Union, Literal, Type, List, ForwardRef, TypeVar, Generic
    _l_(472619)

except ImportError:
    pass

filter_input = { "rules" :
  [{
    "groupOperator" : "and",
    "expressions" : [
      { "field": "xxxxx", "operator": "eq", "value": 'level1' },
      { "field": "xxxxx", "operator": "eq", "value": 'm'},
      { "field": "xxxxx", "operator": "eq", "value": "test"},
      {
        "groupOperator" : "or",
        "expressions" : [
          { "field": "xxxx", "operator": "eq", "value": 'level2' },
          { "field": "xxxx", "operator": "eq", "value": 'm' },
          { "field": "xxxx", "operator": "eq", "value": "test" }
        ]
      }
    ]
  }]
}
_l_(472620)