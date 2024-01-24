# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47405131/flask-type-error-list-object-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(613666, _a_(613665, _n_(613664, "app", lambda: app), "route"), '/DeleteRow', methods=['POST'])
def signUpUser():
    _l_(613679)

    if _a_(613668, _n_(613667, "request", lambda: request), "method") == "POST":
        _l_(613674)

        clicked=_c_(613672, _a_(613671, _a_(613670, _n_(613669, "request", lambda: request), "form"), "getlist"), 'id[]')
        _l_(613673)
    _c_(613677, _n_(613675, "print", lambda: print), _n_(613676, "clicked", lambda: clicked)[0])
    _l_(613678)