# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72453120/typeerror-unhashable-type-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Solution:
    _l_(361812)

    def search(self, nums: List[_n_(361760, "int", lambda: int)], target: _n_(361761, "int", lambda: int)) -> _n_(361762, "int", lambda: int):
        _l_(361811)

        middle = _c_(361767, _n_(361763, "int", lambda: int), _c_(361766, _n_(361764, "len", lambda: len), _n_(361765, "nums", lambda: nums))/2)
        _l_(361768)
        ind = -1
        _l_(361769)
        
        if(_n_(361770, "nums", lambda: nums)[_n_(361771, "middle", lambda: middle)] == _n_(361772, "target", lambda: target)):
            _l_(361810)

            aux = _n_(361773, "ind", lambda: ind)
            _l_(361774)
            return aux
        elif (_n_(361775, "nums", lambda: nums)[_n_(361776, "middle", lambda: middle)] > _n_(361777, "target", lambda: target)):
            _l_(361809)

            ind = _n_(361778, "middle", lambda: middle)
            _l_(361779)
            nums = _n_(361780, "nums", lambda: nums)[:_n_(361781, "middle", lambda: middle)-1]
            _l_(361782)
            _c_(361785, _n_(361783, "print", lambda: print), _n_(361784, "nums", lambda: nums))
            _l_(361786)
            _c_(361790, _n_(361787, "search", lambda: search), _n_(361788, "nums", lambda: nums), _n_(361789, "target", lambda: target))
            _l_(361791)
        else:
            ind = _n_(361792, "middle", lambda: middle)
            _l_(361793)
            nums = _n_(361794, "nums", lambda: nums)[_n_(361795, "middle", lambda: middle):_c_(361798, _n_(361796, "len", lambda: len), _n_(361797, "nums", lambda: nums))-1]
            _l_(361799)
            _c_(361802, _n_(361800, "print", lambda: print), _n_(361801, "nums", lambda: nums))
            _l_(361803)
            _c_(361807, _n_(361804, "search", lambda: search), _n_(361805, "nums", lambda: nums), _n_(361806, "target", lambda: target))
            _l_(361808)