# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58236685/request-headers-gives-typeerror-environheaders-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(412598, _a_(412597, _n_(412596, "app", lambda: app), "route"), '/auth', methods=['GET'])
def auth():
    _l_(412604)

    aux = _c_(412602, _a_(412601, _a_(412600, _n_(412599, "request", lambda: request), "headers"), "get"), 'x-authorization')
    _l_(412603)
    return aux