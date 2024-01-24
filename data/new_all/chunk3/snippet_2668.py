# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67347765/attributeerror-after-post-request-in-django
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_n_(569307, "csrf_exempt", lambda: csrf_exempt)
def login(request):
    _l_(569323)

    json_data = _c_(569314, _a_(569309, _n_(569308, "json", lambda: json), "loads"), _c_(569313, _a_(569312, _a_(569311, _n_(569310, "request", lambda: request), "body"), "decode"), 'utf-8'))
    _l_(569315)
    _c_(569318, _n_(569316, "print", lambda: print), _n_(569317, "json_data", lambda: json_data))
    _l_(569319)
    aux = _a_(569321, _n_(569320, "request", lambda: request), "body")
    _l_(569322)
    return aux