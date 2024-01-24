# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48374582/rest-api-post-request-causing-attributeerror-bytes-object-has-no-attribute-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from urllib.request import Request, urlopen
    _l_(386460)

except ImportError:
    pass
try:
    from urllib.parse import urlencode
    _l_(386462)

except ImportError:
    pass

headers = {
  'Content-Type':'application/json',
  'X-API-KEY':'mykey',
  'X-API-SECRET':'mysecretkey'
}
_l_(386463)

values = {
"exchange_code": "BINA",
"exchange_market": "BTC/USDT",
"type": "all"
}
_l_(386464)


values = _c_(386469, _a_(386468, _c_(386467, _n_(386465, "urlencode", lambda: urlencode), _n_(386466, "values", lambda: values)), "encode"), "utf-8")
_l_(386470)
headers = _c_(386475, _a_(386474, _c_(386473, _n_(386471, "urlencode", lambda: urlencode), _n_(386472, "headers", lambda: headers)), "encode"), "utf-8")
_l_(386476)


request = _c_(386480, _n_(386477, "Request", lambda: Request), 'https://api.coinigy.com/api/v1/data', data=_n_(386478, "values", lambda: values), headers=_n_(386479, "headers", lambda: headers))
_l_(386481)
response_body = _c_(386487, _a_(386486, _c_(386485, _n_(386482, "urlopen", lambda: urlopen), _n_(386483, "request", lambda: request),_n_(386484, "values", lambda: values)), "read"))
_l_(386488)
_c_(386491, _n_(386489, "print", lambda: print), _n_(386490, "response_body", lambda: response_body))
_l_(386492)