# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/40000495/how-to-encode-bytes-in-json-json-dumps-throwing-a-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import base64
    _l_(376664)

except ImportError:
    pass
try:
    import json
    _l_(376666)

except ImportError:
    pass

data = {}
_l_(376667)
encoded = _c_(376670, _a_(376669, _n_(376668, "base64", lambda: base64), "b64encode"), b'data to be encoded')
_l_(376671)
_n_(376672, "data", lambda: data)['bytes'] = _n_(376673, "encoded", lambda: encoded)
_l_(376674)

_c_(376680, _n_(376675, "print", lambda: print), _c_(376679, _a_(376677, _n_(376676, "json", lambda: json), "dumps"), _n_(376678, "data", lambda: data)))
_l_(376681)