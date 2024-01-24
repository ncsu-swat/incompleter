# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56149932/typeerror-in-xmlrpc-client
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class HTTPSDigestAuthTransport:
    _l_(574020)


    def request(self, host, handler, request_body, verbose=0):
        _l_(574019)

        api_url = _c_(573968, _a_(573967, _n_(573966, "Setup", lambda: Setup), "get_api_url"))
        _l_(573969)
        username = _c_(573972, _a_(573971, _n_(573970, "Setup", lambda: Setup), "get_api_username"))
        _l_(573973)
        password = _c_(573976, _a_(573975, _n_(573974, "Setup", lambda: Setup), "get_api_password"))
        _l_(573977)
        h = _c_(573980, _a_(573979, _n_(573978, "httplib2", lambda: httplib2), "Http"))
        _l_(573981)
        if _n_(573982, "verbose", lambda: verbose):
            _l_(573985)

            _n_(573983, "h", lambda: h).debuglevel = 1
            _l_(573984)
        _c_(573990, _a_(573987, _n_(573986, "h", lambda: h), "add_credentials"), _n_(573988, "username", lambda: username), _n_(573989, "password", lambda: password))
        _l_(573991)
        _n_(573992, "h", lambda: h).disable_ssl_certificate_validation = True
        _l_(573993)
        resp, content = _c_(573998, _a_(573995, _n_(573994, "h", lambda: h), "request"), "https://" + _n_(573996, "api_url", lambda: api_url), "POST", body=_n_(573997, "request_body", lambda: request_body),
                              headers={'content-type': 'text/xml'})
        _l_(573999)
        if _a_(574001, _n_(574000, "resp", lambda: resp), "status") != 200:
            _l_(574010)

            raise _c_(574008, _n_(574002, "ProtocolError", lambda: ProtocolError), "https://" + _n_(574003, "api_url", lambda: api_url), _a_(574005, _n_(574004, "resp", lambda: resp), "status"), _a_(574007, _n_(574006, "resp", lambda: resp), "reason"), None)
            _l_(574009)
        p, u = _c_(574012, _n_(574011, "getparser", lambda: getparser), 0)
        _l_(574013)
        _c_(574017, _a_(574015, _n_(574014, "p", lambda: p), "feed"), _n_(574016, "content", lambda: content))
        _l_(574018)


# transport factory instance
transport = _c_(574022, _n_(574021, "HTTPSDigestAuthTransport", lambda: HTTPSDigestAuthTransport))
_l_(574023)

# url composition
url = "https://" + _c_(574026, _a_(574025, _n_(574024, "Setup", lambda: Setup), "get_api_username")) + ":" + _c_(574029, _a_(574028, _n_(574027, "Setup", lambda: Setup), "get_api_password")) + "@" + _c_(574032, _a_(574031, _n_(574030, "Setup", lambda: Setup), "get_api_url"))
_l_(574033)

# create the proxy
proxy = _c_(574039, _a_(574036, _a_(574035, _n_(574034, "xmlrpc", lambda: xmlrpc), "client"), "ServerProxy"), _n_(574037, "url", lambda: url), _n_(574038, "transport", lambda: transport))
_l_(574040)
res = _c_(574043, _a_(574042, _n_(574041, "proxy", lambda: proxy), "do_some_work"))
_l_(574044)