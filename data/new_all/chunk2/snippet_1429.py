# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59871383/why-typeerror-unhashable-type-list-when-calling-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
a = [5,5,6,7,7,7]
_l_(438764)
b = _c_(438767, _n_(438765, "set", lambda: set), _n_(438766, "a", lambda: a))
_l_(438768)
def test(lst):
    _l_(438774)

    if _n_(438769, "lst", lambda: lst) in _n_(438770, "b", lambda: b):
        _l_(438773)

        aux = 1
        _l_(438771)
        return aux
    else:
        aux = 0
        _l_(438772)
        return aux
_c_(438779, _n_(438775, "print", lambda: print), _c_(438778, _n_(438776, "test", lambda: test), _n_(438777, "a", lambda: a)))  #this gives me error list unhashable  
_l_(438780)  #this gives me error list unhashable  
_c_(438784, _n_(438781, "print", lambda: print), _n_(438782, "test", lambda: test),_n_(438783, "a", lambda: a))   #how this is working
_l_(438785)   #how this is working
for i in  _c_(438789, _n_(438786, "filter", lambda: filter), _n_(438787, "test", lambda: test), _n_(438788, "a", lambda: a)):
    _l_(438794)

    _c_(438792, _n_(438790, "print", lambda: print), _n_(438791, "i", lambda: i),end=" ")
    _l_(438793)