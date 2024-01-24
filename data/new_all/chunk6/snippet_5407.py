# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55584454/how-to-fix-type-error-while-concatenating-two-lists
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
MyList = _c_(345924, _n_(345921, "list", lambda: list), _c_(345923, _n_(345922, "range", lambda: range), 1,51))
_l_(345925)
sublist1 = _n_(345926, "MyList", lambda: MyList)[-26:-29:-1]
_l_(345927)
sublist1 = _c_(345930, _a_(345929, _n_(345928, "sublist1", lambda: sublist1), "reverse"))
_l_(345931)
sublist2 = _n_(345932, "MyList", lambda: MyList)[25:27:1]
_l_(345933)
_c_(345937, _n_(345934, "print", lambda: print), _n_(345935, "sublist1", lambda: sublist1) + _n_(345936, "sublist2", lambda: sublist2))
_l_(345938)