# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import defaultdict
    _l_(114672)

except ImportError:
    pass
classes = (('V', 1), ('VI', 1), ('V', 2), ('VI', 2), ('VI', 3), ('VII', 1))
_l_(114673)
for class_name, roll_id in _n_(114674, "classes", lambda: classes):
    _l_(114681)

    _c_(114679, _a_(114677, _n_(114675, "class_rollno", lambda: class_rollno)[_n_(114676, "class_name", lambda: class_name)], "append"), _n_(114678, "roll_id", lambda: roll_id))
    _l_(114680)
_c_(114684, _n_(114682, "print", lambda: print), _n_(114683, "class_rollno", lambda: class_rollno))
_l_(114685)