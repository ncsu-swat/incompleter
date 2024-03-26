# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import defaultdict
    _l_(114654)

except ImportError:
    pass
class_rollno = _c_(114657, _n_(114655, "defaultdict", lambda: defaultdict), _n_(114656, "list", lambda: list))
_l_(114658)
for class_name, roll_id in _n_(114659, "classes", lambda: classes):
    _l_(114666)

    _c_(114664, _a_(114662, _n_(114660, "class_rollno", lambda: class_rollno)[_n_(114661, "class_name", lambda: class_name)], "append"), _n_(114663, "roll_id", lambda: roll_id))
    _l_(114665)
_c_(114669, _n_(114667, "print", lambda: print), _n_(114668, "class_rollno", lambda: class_rollno))
_l_(114670)