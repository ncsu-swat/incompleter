# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def list_of_dicts(marks):
    _l_(68492)

    keys = _c_(68474, _a_(68473, _n_(68472, "marks", lambda: marks), "keys"))
    _l_(68475)
    vals = _c_(68480, _n_(68476, "zip", lambda: zip), *[_n_(68477, "marks", lambda: marks)[_n_(68478, "k", lambda: k)] for k in _n_(68479, "keys", lambda: keys)])
    _l_(68481)
    result = [_c_(68487, _n_(68482, "dict", lambda: dict), _c_(68486, _n_(68483, "zip", lambda: zip), _n_(68484, "keys", lambda: keys), _n_(68485, "v", lambda: v))) for v in _n_(68488, "vals", lambda: vals)]
    _l_(68489)
    aux = _n_(68490, "result", lambda: result)
    _l_(68491)
    return aux
_c_(68494, _n_(68493, "print", lambda: print), 'Original dictionary of lists:')
_l_(68495)
_c_(68498, _n_(68496, "print", lambda: print), _n_(68497, "marks", lambda: marks))
_l_(68499)
_c_(68501, _n_(68500, "print", lambda: print), '\nSplit said dictionary of lists into list of dictionaries:')
_l_(68502)
_c_(68507, _n_(68503, "print", lambda: print), _c_(68506, _n_(68504, "list_of_dicts", lambda: list_of_dicts), _n_(68505, "marks", lambda: marks)))
_l_(68508)