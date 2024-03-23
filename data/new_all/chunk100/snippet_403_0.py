# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import defaultdict
    _l_(39720)

except ImportError:
    pass
classes = (('V', 1), ('VI', 1), ('V', 2), ('VI', 2), ('VI', 3), ('VII', 1))
_l_(39721)
for (class_name, roll_id) in _n_(39722, "classes", lambda: classes):
    _l_(39729)

    _c_(39727, _a_(39725, _n_(39723, "class_rollno", lambda: class_rollno)[_n_(39724, "class_name", lambda: class_name)], "append"), _n_(39726, "roll_id", lambda: roll_id))
    _l_(39728)
_c_(39732, _n_(39730, "print", lambda: print), _n_(39731, "class_rollno", lambda: class_rollno))
_l_(39733)