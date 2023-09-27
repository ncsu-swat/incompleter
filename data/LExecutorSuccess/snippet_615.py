# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/26745519/converting-dictionary-to-json
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(1540711)

except ImportError:
    pass

r = {'is_claimed': 'True', 'rating': 3.5}
_l_(1540712)
r = _c_(1540716, _a_(1540714, _n_(1540713, "json", lambda: json), "dumps"), _n_(1540715, "r", lambda: r))
_l_(1540717)
loaded_r = _c_(1540721, _a_(1540719, _n_(1540718, "json", lambda: json), "loads"), _n_(1540720, "r", lambda: r))
_l_(1540722)
_n_(1540723, "loaded_r", lambda: loaded_r)['rating'] #Output 3.5
_l_(1540724) #Output 3.5
_c_(1540727, _n_(1540725, "type", lambda: type), _n_(1540726, "r", lambda: r)) #Output str
_l_(1540728) #Output str
_c_(1540731, _n_(1540729, "type", lambda: type), _n_(1540730, "loaded_r", lambda: loaded_r)) #Output dict
_l_(1540732) #Output dict

