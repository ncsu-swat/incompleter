# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61214984/interger-list-reversal-producing-a-nonetype-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
some_numbers = [1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77]
_l_(684285)

reversed_numbers = []
_l_(684286)

i = 0
_l_(684287)

while _n_(684288, "some_numbers", lambda: some_numbers):
    _l_(684299)

    reversed_numbers = _c_(684295, _a_(684290, _n_(684289, "reversed_numbers", lambda: reversed_numbers), "insert"), _n_(684291, "i", lambda: i), _c_(684294, _a_(684293, _n_(684292, "some_numbers", lambda: some_numbers), "pop")))
    _l_(684296)
    i = _n_(684297, "i", lambda: i) + 1
    _l_(684298)


_c_(684302, _n_(684300, "print", lambda: print), _n_(684301, "reversed_numbers", lambda: reversed_numbers))
_l_(684303)