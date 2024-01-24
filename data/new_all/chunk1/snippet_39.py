# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63460126/typeerror-type-object-is-not-subscriptable-in-a-function-signature
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
nums = [4,5,6,7,8,9]
_l_(409026)
target = 13
_l_(409027)

def twoSum(self, nums: _n_(409028, "list", lambda: list)[_n_(409029, "int", lambda: int)], target: _n_(409030, "int", lambda: int)) -> _n_(409031, "list", lambda: list)[_n_(409032, "int", lambda: int)]:
        _l_(409070)

        dictionary = {}
        _l_(409033)
        answer = []
        _l_(409034)
 
        for i in _c_(409039, _n_(409035, "range", lambda: range), _c_(409038, _n_(409036, "len", lambda: len), _n_(409037, "nums", lambda: nums))):
                _l_(409069)

                secondNumber = _n_(409040, "target", lambda: target)-_n_(409041, "nums", lambda: nums)[_n_(409042, "i", lambda: i)]
                _l_(409043)
                if(_n_(409044, "secondNumber", lambda: secondNumber) in _c_(409047, _a_(409046, _n_(409045, "dictionary", lambda: dictionary), "keys"))):
                        _l_(409061)

                        secondIndex = _c_(409051, _a_(409049, _n_(409048, "nums", lambda: nums), "index"), _n_(409050, "secondNumber", lambda: secondNumber))
                        _l_(409052)
                        if(_n_(409053, "i", lambda: i) != _n_(409054, "secondIndex", lambda: secondIndex)):
                                _l_(409060)

                                aux = _c_(409058, _n_(409055, "sorted", lambda: sorted), [_n_(409056, "i", lambda: i), _n_(409057, "secondIndex", lambda: secondIndex)])
                                _l_(409059)
                                return aux
                _c_(409067, _a_(409063, _n_(409062, "dictionary", lambda: dictionary), "update"), {_n_(409064, "nums", lambda: nums)[_n_(409065, "i", lambda: i)]: _n_(409066, "i", lambda: i)})
                _l_(409068)

_c_(409076, _n_(409071, "print", lambda: print), _c_(409075, _n_(409072, "twoSum", lambda: twoSum), _n_(409073, "nums", lambda: nums), _n_(409074, "target", lambda: target)))
_l_(409077)