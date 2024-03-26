# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
student_data = {'id1': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']}, 'id2': {'name': ['David'], 'class': ['V'], 'subject_integration': ['english, math, science']}, 'id3': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']}, 'id4': {'name': ['Surya'], 'class': ['V'], 'subject_integration': ['english, math, science']}}
_l_(119544)
for key, value in _c_(119547, _a_(119546, _n_(119545, "student_data", lambda: student_data), "items")):
    _l_(119557)

    if _n_(119548, "value", lambda: value) not in _c_(119551, _a_(119550, _n_(119549, "result", lambda: result), "values")):
        _l_(119556)

        _n_(119552, "result", lambda: result)[_n_(119553, "key", lambda: key)] = _n_(119554, "value", lambda: value)
        _l_(119555)
_c_(119560, _n_(119558, "print", lambda: print), _n_(119559, "result", lambda: result))
_l_(119561)