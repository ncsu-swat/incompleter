# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58086723/python-urllib-request-urlopen-attributeerror-bytes-object-has-no-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
api_url = _a_(388094, _n_(388093, "self", lambda: self), "api_base")+'/street2coordinates'
_l_(388095)
api_body = _c_(388099, _a_(388097, _n_(388096, "json", lambda: json), "dumps"), _n_(388098, "addresses", lambda: addresses))
_l_(388100)
#api_url=api_url.encode("utf-8")
#api_body=api_body.encode("utf-8")
_c_(388105, _n_(388101, "print", lambda: print), _c_(388104, _n_(388102, "type", lambda: type), _n_(388103, "api_url", lambda: api_url)))
_l_(388106)
response_string = _c_(388116, _a_(388115, _c_(388114, _a_(388111, _a_(388110, _a_(388109, _a_(388108, _n_(388107, "six", lambda: six), "moves"), "urllib"), "request"), "urlopen"), _n_(388112, "api_url", lambda: api_url), _n_(388113, "api_body", lambda: api_body)), "read"))
_l_(388117)
response = _c_(388121, _a_(388119, _n_(388118, "json", lambda: json), "loads"), _n_(388120, "response_string", lambda: response_string))
_l_(388122)