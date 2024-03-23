# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import collections
    _l_(78348)

except ImportError:
    pass

class Solution(_n_(78349, "object", lambda: object)):
    _l_(78360)


    def majorityElement(self, nums):
        _l_(78359)

        """
        :type nums: List[int]
        :return type: int
        """
        count_ele = _c_(78353, _a_(78351, _n_(78350, "collections", lambda: collections), "Counter"), _n_(78352, "nums", lambda: nums))
        _l_(78354)
        aux = _c_(78357, _a_(78356, _n_(78355, "count_ele", lambda: count_ele), "most_common"))[0][0]
        _l_(78358)
        return aux
_c_(78363, _n_(78361, "print", lambda: print), _n_(78362, "result", lambda: result))
_l_(78364)