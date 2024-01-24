# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58012400/compiling-json-schema-using-fastjsonschema-gives-typeerror-string-indices-must
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import fastjsonschema
    _l_(550128)

except ImportError:
    pass

schema_file = _c_(550132, _n_(550129, "open", lambda: open), _a_(550131, _n_(550130, "schema", lambda: schema), "json"))
_l_(550133)
schema_str = _c_(550136, _a_(550135, _n_(550134, "schema_file", lambda: schema_file), "read"))
_l_(550137)
validatation = _c_(550141, _a_(550139, _n_(550138, "fastjsonschema", lambda: fastjsonschema), "compile"), _n_(550140, "schema_str", lambda: schema_str))
_l_(550142)