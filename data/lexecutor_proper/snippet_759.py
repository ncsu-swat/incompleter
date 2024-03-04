# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/17043860/how-to-dump-a-dict-to-a-json-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
d = {"name":"interpolator",
     "children":[{'name':_n_(64706, "key", lambda: key),"size":_n_(64707, "value", lambda: value)} for key,value in _c_(64710, _a_(64709, _n_(64708, "sample", lambda: sample), "items"))]}
_l_(64711)
json_string = _c_(64715, _a_(64713, _n_(64712, "json", lambda: json), "dumps"), _n_(64714, "d", lambda: d))
_l_(64716)

