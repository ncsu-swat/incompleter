# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/23679092/typeerror-int-argument-must-be-a-string-or-a-number-not-list-please
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
testfile = _c_(345719, _n_(345717, "open", lambda: open), _n_(345718, "fname", lambda: fname), 'r+')
_l_(345720)
new_ingrediants = _c_(345722, _n_(345721, "input", lambda: input), "How Many People Do You Want To Recalculate For?")
_l_(345723)
new_ingrediants = _c_(345726, _n_(345724, "int", lambda: int), _n_(345725, "new_ingrediants", lambda: new_ingrediants))
_l_(345727)
ingrediant1 = _c_(345732, _a_(345731, _c_(345730, _n_(345728, "open", lambda: open), _n_(345729, "fname", lambda: fname)), "readlines"), 3)
_l_(345733)
ingrediant1 = _c_(345736, _n_(345734, "int", lambda: int), _n_(345735, "ingrediant1", lambda: ingrediant1))
_l_(345737)
new_ingrediant1 = (_n_(345738, "ingrediant1", lambda: ingrediant1)*_n_(345739, "new_ingrediants", lambda: new_ingrediants))
_l_(345740)
_c_(345743, _n_(345741, "print", lambda: print), _n_(345742, "new_ingrediant1", lambda: new_ingrediant1))
_l_(345744)