# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62973342/how-can-i-fix-this-error-typeerror-list-object-is-not-callable-on-line-17
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def last_four(x):
    _l_(571298)

    aux = _n_(571296, "x", lambda: x)[-4:]
    _l_(571297)
    return aux

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
_l_(571299)
ids2=[]
_l_(571300)
for i in _n_(571301, "ids", lambda: ids):
    _l_(571309)

    _c_(571307, _a_(571303, _n_(571302, "ids2", lambda: ids2), "append"), _c_(571306, _n_(571304, "str", lambda: str), _n_(571305, "i", lambda: i)))
    _l_(571308)
sorted_ids=_c_(571315, _n_(571310, "sorted", lambda: sorted), _n_(571311, "ids2", lambda: ids2),key=_c_(571314, _n_(571312, "last_four", lambda: last_four), _n_(571313, "ids2", lambda: ids2)))
_l_(571316)
_c_(571319, _n_(571317, "print", lambda: print), _n_(571318, "sorted_ids", lambda: sorted_ids))
_l_(571320)