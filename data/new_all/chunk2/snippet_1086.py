# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/36378643/gmail-api-typeerror-sequence-item-0-expected-str-instance-bytes-found
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
credentials = _c_(444127, _n_(444126, "get_credentials", lambda: get_credentials))
_l_(444128)
_c_(444131, _n_(444129, "print", lambda: print), _n_(444130, "credentials", lambda: credentials))
_l_(444132)
_c_(444138, _n_(444133, "print", lambda: print), _c_(444137, _n_(444134, "str", lambda: str), _a_(444136, _n_(444135, "credentials", lambda: credentials), "invalid")))
_l_(444139)
http = _c_(444145, _a_(444141, _n_(444140, "credentials", lambda: credentials), "authorize"), _c_(444144, _a_(444143, _n_(444142, "httplib2", lambda: httplib2), "Http")))
_l_(444146)
service = _c_(444150, _a_(444148, _n_(444147, "discovery", lambda: discovery), "build"), 'gmail', 'v1', http=_n_(444149, "http", lambda: http))
_l_(444151)