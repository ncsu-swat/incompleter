# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import collections
    _l_(78330)

except ImportError:
    pass

class Solution(_n_(78331, "object", lambda: object)):
    _l_(78337)


    def majorityElement(self, nums):
        _l_(78336)

        """
        :type nums: List[int]
        :return type: int
        """
        aux = _c_(78334, _a_(78333, _n_(78332, "count_ele", lambda: count_ele), "most_common"))[0][0]
        _l_(78335)
        return aux
result = _c_(78341, _a_(78340, _c_(78339, _n_(78338, "Solution", lambda: Solution)), "majorityElement"), [10, 10, 20, 30, 40, 10, 20, 10])
_l_(78342)
_c_(78345, _n_(78343, "print", lambda: print), _n_(78344, "result", lambda: result))
_l_(78346)