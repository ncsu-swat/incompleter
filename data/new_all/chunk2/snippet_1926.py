# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/27995090/typeerror-raised-by-bytes-join-when-passing-in-a-byte-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
header = _c_(421616, _a_(421607, _n_(421606, "struct", lambda: struct), "pack"), _n_(421608, "STRFMT", lambda: STRFMT), _n_(421609, "MAGIC", lambda: MAGIC), _n_(421610, "VERSION", lambda: VERSION),
            _n_(421611, "command", lambda: command), _a_(421613, _n_(421612, "self", lambda: self), "seq"), _a_(421615, _n_(421614, "self", lambda: self), "session"))
_l_(421617)

data = _c_(421620, _a_(421619, _n_(421618, "dataStr", lambda: dataStr), "encode")) # dataStr is a String
_l_(421621) # dataStr is a String

_c_(421626, _n_(421622, "print", lambda: print), _c_(421625, _n_(421623, "type", lambda: type), _n_(421624, "header", lambda: header))) # <class 'bytes'>
_l_(421627) # <class 'bytes'>
_c_(421632, _n_(421628, "print", lambda: print), _c_(421631, _n_(421629, "type", lambda: type), _n_(421630, "header", lambda: header))) # <class 'bytes'>
_l_(421633) # <class 'bytes'>

_c_(421637, _a_(421635, _n_(421634, "header", lambda: header), "join"), _n_(421636, "data", lambda: data))
_l_(421638)