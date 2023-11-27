# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5384914/how-do-i-delete-items-from-a-dictionary-while-iterating-over-it
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
dict = {'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4}
_l_(1544976)
delete = []
_l_(1544977)
for k,v in _c_(1544980, _a_(1544979, _n_(1544978, "dict", lambda: dict), "items")):
    _l_(1544988)

    if _n_(1544981, "v", lambda: v)%2 == 1:
        _l_(1544987)

        _c_(1544985, _a_(1544983, _n_(1544982, "delete", lambda: delete), "append"), _n_(1544984, "k", lambda: k))
        _l_(1544986)
for i in _n_(1544989, "delete", lambda: delete):
    _l_(1544991)

    del dict[i]
    _l_(1544990)

