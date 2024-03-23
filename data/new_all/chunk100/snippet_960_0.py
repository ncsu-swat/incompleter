# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
text = ['a', 'b', 'c', 'd', 'e', 'f']
_l_(96290)
_c_(96292, _n_(96291, "print", lambda: print), 'Original list:')
_l_(96293)
_c_(96296, _n_(96294, "print", lambda: print), _n_(96295, "text", lambda: text))
_l_(96297)
_c_(96299, _n_(96298, "print", lambda: print), '\nDisplay each element vertically of the said list:')
_l_(96300)
for i in _n_(96301, "text", lambda: text):
    _l_(96306)

    _c_(96304, _n_(96302, "print", lambda: print), _n_(96303, "i", lambda: i))
    _l_(96305)
_c_(96308, _n_(96307, "print", lambda: print), 'Original list:')
_l_(96309)
_c_(96312, _n_(96310, "print", lambda: print), _n_(96311, "nums", lambda: nums))
_l_(96313)
_c_(96315, _n_(96314, "print", lambda: print), '\nDisplay each element vertically of the said list of lists:')
_l_(96316)
for (a, b, c) in _c_(96319, _n_(96317, "zip", lambda: zip), *_n_(96318, "nums", lambda: nums)):
    _l_(96326)

    _c_(96324, _n_(96320, "print", lambda: print), _n_(96321, "a", lambda: a), _n_(96322, "b", lambda: b), _n_(96323, "c", lambda: c))
    _l_(96325)