# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import defaultdict
    _l_(39735)

except ImportError:
    pass
class_rollno = _c_(39738, _n_(39736, "defaultdict", lambda: defaultdict), _n_(39737, "list", lambda: list))
_l_(39739)
for (class_name, roll_id) in _n_(39740, "classes", lambda: classes):
    _l_(39747)

    _c_(39745, _a_(39743, _n_(39741, "class_rollno", lambda: class_rollno)[_n_(39742, "class_name", lambda: class_name)], "append"), _n_(39744, "roll_id", lambda: roll_id))
    _l_(39746)
_c_(39750, _n_(39748, "print", lambda: print), _n_(39749, "class_rollno", lambda: class_rollno))
_l_(39751)