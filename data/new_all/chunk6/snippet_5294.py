# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72453120/typeerror-unhashable-type-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Solution:
    _l_(348447)

    def search(self, nums: List[_n_(348395, "int", lambda: int)], target: _n_(348396, "int", lambda: int)) -> _n_(348397, "int", lambda: int):
        _l_(348446)

        middle = _c_(348402, _n_(348398, "int", lambda: int), _c_(348401, _n_(348399, "len", lambda: len), _n_(348400, "nums", lambda: nums))/2)
        _l_(348403)
        ind = -1
        _l_(348404)
        
        if(_n_(348405, "nums", lambda: nums)[_n_(348406, "middle", lambda: middle)] == _n_(348407, "target", lambda: target)):
            _l_(348445)

            aux = _n_(348408, "ind", lambda: ind)
            _l_(348409)
            return aux
        elif (_n_(348410, "nums", lambda: nums)[_n_(348411, "middle", lambda: middle)] > _n_(348412, "target", lambda: target)):
            _l_(348444)

            ind = _n_(348413, "middle", lambda: middle)
            _l_(348414)
            nums = _n_(348415, "nums", lambda: nums)[:_n_(348416, "middle", lambda: middle)-1]
            _l_(348417)
            _c_(348420, _n_(348418, "print", lambda: print), _n_(348419, "nums", lambda: nums))
            _l_(348421)
            _c_(348425, _n_(348422, "search", lambda: search), _n_(348423, "nums", lambda: nums), _n_(348424, "target", lambda: target))
            _l_(348426)
        else:
            ind = _n_(348427, "middle", lambda: middle)
            _l_(348428)
            nums = _n_(348429, "nums", lambda: nums)[_n_(348430, "middle", lambda: middle):_c_(348433, _n_(348431, "len", lambda: len), _n_(348432, "nums", lambda: nums))-1]
            _l_(348434)
            _c_(348437, _n_(348435, "print", lambda: print), _n_(348436, "nums", lambda: nums))
            _l_(348438)
            _c_(348442, _n_(348439, "search", lambda: search), _n_(348440, "nums", lambda: nums), _n_(348441, "target", lambda: target))
            _l_(348443)