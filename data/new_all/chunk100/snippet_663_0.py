# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def list_of_dicts(marks):
    _l_(68454)

    keys = _c_(68444, _a_(68443, _n_(68442, "marks", lambda: marks), "keys"))
    _l_(68445)
    vals = _c_(68450, _n_(68446, "zip", lambda: zip), *[_n_(68447, "marks", lambda: marks)[_n_(68448, "k", lambda: k)] for k in _n_(68449, "keys", lambda: keys)])
    _l_(68451)
    aux = _n_(68452, "result", lambda: result)
    _l_(68453)
    return aux
marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
_l_(68455)
_c_(68457, _n_(68456, "print", lambda: print), 'Original dictionary of lists:')
_l_(68458)
_c_(68461, _n_(68459, "print", lambda: print), _n_(68460, "marks", lambda: marks))
_l_(68462)
_c_(68464, _n_(68463, "print", lambda: print), '\nSplit said dictionary of lists into list of dictionaries:')
_l_(68465)
_c_(68470, _n_(68466, "print", lambda: print), _c_(68469, _n_(68467, "list_of_dicts", lambda: list_of_dicts), _n_(68468, "marks", lambda: marks)))
_l_(68471)