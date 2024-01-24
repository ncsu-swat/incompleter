# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56333685/typeerror-unhashable-type-set-in-http-get-request
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def getInvoice(inv_id):
    _l_(666162)

    response = _c_(666158, _a_(666157, _c_(666156, _a_(666152, _n_(666151, "requests", lambda: requests), "get"), "https://api.example.com/invoices/"+_c_(666155, _n_(666153, "str", lambda: str), _n_(666154, "inv_id", lambda: inv_id))+"?access_token=123456789"), "json"))
    _l_(666159)
    aux = _n_(666160, "response", lambda: response)
    _l_(666161)
    return aux

_c_(666166, _n_(666163, "print", lambda: print), _c_(666165, _n_(666164, "getInvoice", lambda: getInvoice), "5b5f60384b3f"))
_l_(666167)