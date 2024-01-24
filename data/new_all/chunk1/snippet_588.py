# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62807109/python-json-attributeerror-str-object-has-no-attribute-read
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(384106)

except ImportError:
    pass
fil='numbers.json'
_l_(384107)
num=[]
_l_(384108)
with _c_(384111, _n_(384109, "open", lambda: open), _n_(384110, "fil", lambda: fil),'r') as file :
    _l_(384122)

    for obj in _n_(384112, "file", lambda: file) :
        _l_(384121)

        _c_(384119, _a_(384114, _n_(384113, "num", lambda: num), "append"), _c_(384118, _a_(384116, _n_(384115, "json", lambda: json), "load"), _n_(384117, "obj", lambda: obj)))
        _l_(384120)
_c_(384125, _n_(384123, "print", lambda: print), _n_(384124, "num", lambda: num))
_l_(384126)