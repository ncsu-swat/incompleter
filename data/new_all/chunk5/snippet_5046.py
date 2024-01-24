# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61214984/interger-list-reversal-producing-a-nonetype-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
some_numbers = [1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77]
_l_(692287)

reversed_numbers = []
_l_(692288)

i = 0
_l_(692289)

while _n_(692290, "some_numbers", lambda: some_numbers):
    _l_(692301)

    reversed_numbers = _c_(692297, _a_(692292, _n_(692291, "reversed_numbers", lambda: reversed_numbers), "insert"), _n_(692293, "i", lambda: i), _c_(692296, _a_(692295, _n_(692294, "some_numbers", lambda: some_numbers), "pop")))
    _l_(692298)
    i = _n_(692299, "i", lambda: i) + 1
    _l_(692300)


_c_(692304, _n_(692302, "print", lambda: print), _n_(692303, "reversed_numbers", lambda: reversed_numbers))
_l_(692305)