# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56333685/typeerror-unhashable-type-set-in-http-get-request
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def getInvoice(inv_id):
    _l_(671722)

    response = _c_(671718, _a_(671717, _c_(671716, _a_(671712, _n_(671711, "requests", lambda: requests), "get"), "https://api.example.com/invoices/"+_c_(671715, _n_(671713, "str", lambda: str), _n_(671714, "inv_id", lambda: inv_id))+"?access_token=123456789"), "json"))
    _l_(671719)
    aux = _n_(671720, "response", lambda: response)
    _l_(671721)
    return aux

_c_(671726, _n_(671723, "print", lambda: print), _c_(671725, _n_(671724, "getInvoice", lambda: getInvoice), "5b5f60384b3f"))
_l_(671727)