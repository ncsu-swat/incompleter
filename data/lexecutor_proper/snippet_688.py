# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/19125722/adding-a-legend-to-pyplot-in-matplotlib-in-the-simplest-manner-possible
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
first = [1, 2, 4, 5, 4]
_l_(64275)
second = [3, 4, 2, 2, 3]
_l_(64276)
_c_(64281, _a_(64278, _n_(64277, "plt", lambda: plt), "plot"), _n_(64279, "first", lambda: first), 'g--', _n_(64280, "second", lambda: second), 'r--')
_l_(64282)
_c_(64285, _a_(64284, _n_(64283, "plt", lambda: plt), "legend"), ['First List', 'Second List'], loc='upper left')
_l_(64286)
_c_(64289, _a_(64288, _n_(64287, "plt", lambda: plt), "show"))
_l_(64290)

