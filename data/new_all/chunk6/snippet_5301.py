# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72453120/typeerror-unhashable-type-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Solution:
    _l_(359990)

    def search(self, nums: List[_n_(359938, "int", lambda: int)], target: _n_(359939, "int", lambda: int)) -> _n_(359940, "int", lambda: int):
        _l_(359989)

        middle = _c_(359945, _n_(359941, "int", lambda: int), _c_(359944, _n_(359942, "len", lambda: len), _n_(359943, "nums", lambda: nums))/2)
        _l_(359946)
        ind = -1
        _l_(359947)
        
        if(_n_(359948, "nums", lambda: nums)[_n_(359949, "middle", lambda: middle)] == _n_(359950, "target", lambda: target)):
            _l_(359988)

            aux = _n_(359951, "ind", lambda: ind)
            _l_(359952)
            return aux
        elif (_n_(359953, "nums", lambda: nums)[_n_(359954, "middle", lambda: middle)] > _n_(359955, "target", lambda: target)):
            _l_(359987)

            ind = _n_(359956, "middle", lambda: middle)
            _l_(359957)
            nums = _n_(359958, "nums", lambda: nums)[:_n_(359959, "middle", lambda: middle)-1]
            _l_(359960)
            _c_(359963, _n_(359961, "print", lambda: print), _n_(359962, "nums", lambda: nums))
            _l_(359964)
            _c_(359968, _n_(359965, "search", lambda: search), _n_(359966, "nums", lambda: nums), _n_(359967, "target", lambda: target))
            _l_(359969)
        else:
            ind = _n_(359970, "middle", lambda: middle)
            _l_(359971)
            nums = _n_(359972, "nums", lambda: nums)[_n_(359973, "middle", lambda: middle):_c_(359976, _n_(359974, "len", lambda: len), _n_(359975, "nums", lambda: nums))-1]
            _l_(359977)
            _c_(359980, _n_(359978, "print", lambda: print), _n_(359979, "nums", lambda: nums))
            _l_(359981)
            _c_(359985, _n_(359982, "search", lambda: search), _n_(359983, "nums", lambda: nums), _n_(359984, "target", lambda: target))
            _l_(359986)