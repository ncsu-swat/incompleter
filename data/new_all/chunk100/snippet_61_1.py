# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
student_data = {'id1': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']}, 'id2': {'name': ['David'], 'class': ['V'], 'subject_integration': ['english, math, science']}, 'id3': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']}, 'id4': {'name': ['Surya'], 'class': ['V'], 'subject_integration': ['english, math, science']}}
_l_(64842)
for (key, value) in _c_(64845, _a_(64844, _n_(64843, "student_data", lambda: student_data), "items")):
    _l_(64855)

    if _n_(64846, "value", lambda: value) not in _c_(64849, _a_(64848, _n_(64847, "result", lambda: result), "values")):
        _l_(64854)

        _n_(64850, "result", lambda: result)[_n_(64851, "key", lambda: key)] = _n_(64852, "value", lambda: value)
        _l_(64853)
_c_(64858, _n_(64856, "print", lambda: print), _n_(64857, "result", lambda: result))
_l_(64859)