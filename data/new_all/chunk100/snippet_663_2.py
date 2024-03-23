# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def list_of_dicts(marks):
    _l_(68523)

    keys = _c_(68511, _a_(68510, _n_(68509, "marks", lambda: marks), "keys"))
    _l_(68512)
    result = [_c_(68518, _n_(68513, "dict", lambda: dict), _c_(68517, _n_(68514, "zip", lambda: zip), _n_(68515, "keys", lambda: keys), _n_(68516, "v", lambda: v))) for v in _n_(68519, "vals", lambda: vals)]
    _l_(68520)
    aux = _n_(68521, "result", lambda: result)
    _l_(68522)
    return aux
marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
_l_(68524)
_c_(68526, _n_(68525, "print", lambda: print), 'Original dictionary of lists:')
_l_(68527)
_c_(68530, _n_(68528, "print", lambda: print), _n_(68529, "marks", lambda: marks))
_l_(68531)
_c_(68533, _n_(68532, "print", lambda: print), '\nSplit said dictionary of lists into list of dictionaries:')
_l_(68534)
_c_(68539, _n_(68535, "print", lambda: print), _c_(68538, _n_(68536, "list_of_dicts", lambda: list_of_dicts), _n_(68537, "marks", lambda: marks)))
_l_(68540)