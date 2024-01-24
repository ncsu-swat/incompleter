# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63046056/im-trying-to-print-a-list-it-gives-type-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
buyList = ["Potato", "Suger", "Rice", "Oil", "Cake", "Biscuit"]
_l_(546923)

for i in _n_(546924, "buyList", lambda: buyList):
    _l_(546932)

    if _n_(546925, "i", lambda: i) % 2 is not 0:
        _l_(546931)

        _c_(546928, _n_(546926, "print", lambda: print), _n_(546927, "i", lambda: i), end=" ")
        _l_(546929)
        i += 1
        _l_(546930)