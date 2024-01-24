# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69696035/typeerror-object-of-type-mappingproxy-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import streamlit as st
    _l_(590359)

except ImportError:
    pass
try:
    import Processor as processor
    _l_(590361)

except ImportError:
    pass
try:
    import json
    _l_(590363)

except ImportError:
    pass

ecgProperty = _c_(590366, _a_(590365, _n_(590364, "processor", lambda: processor), "GetSourceProperty"), r"C:\Users\100.dat")
_l_(590367)

_c_(590373, _a_(590369, _n_(590368, "st", lambda: st), "write"), _c_(590372, _n_(590370, "type", lambda: type), _n_(590371, "ecgProperty", lambda: ecgProperty)))
_l_(590374)
_c_(590378, _a_(590376, _n_(590375, "st", lambda: st), "write"), _n_(590377, "ecgProperty", lambda: ecgProperty))
_l_(590379)
jsonECGPropertyStr = _c_(590384, _a_(590381, _n_(590380, "json", lambda: json), "dumps"), _a_(590383, _n_(590382, "ecgProperty", lambda: ecgProperty), "__dict__"))
_l_(590385)
_c_(590389, _a_(590387, _n_(590386, "st", lambda: st), "write"), _n_(590388, "jsonECGPropertyStr", lambda: jsonECGPropertyStr))
_l_(590390)