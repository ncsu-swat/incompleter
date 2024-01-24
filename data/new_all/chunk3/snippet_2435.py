# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/39329074/attributeerror-request-object-has-no-attribute-params
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from wsgiref import simple_server
    _l_(553208)

except ImportError:
    pass
try:
    import falcon
    _l_(553210)

except ImportError:
    pass

class user(_n_(553211, "object", lambda: object)):
    _l_(553218)

    def on_get(self, req, resp):
        _l_(553217)

        _c_(553215, _n_(553212, "print", lambda: print), _a_(553214, _n_(553213, "req", lambda: req), "params")['name'])
        _l_(553216)

api = application = _c_(553221, _a_(553220, _n_(553219, "falcon", lambda: falcon), "API"))
_l_(553222)

usr = _c_(553224, _n_(553223, "user", lambda: user))
_l_(553225)
_c_(553229, _a_(553227, _n_(553226, "api", lambda: api), "add_route"), '/user', _n_(553228, "usr", lambda: usr))
_l_(553230)

if _n_(553231, "__name__", lambda: __name__) == '__main__':
    _l_(553241)

    http = _c_(553235, _a_(553233, _n_(553232, "simple_server", lambda: simple_server), "make_server"), '127.0.0.10', 8000, _n_(553234, "api", lambda: api))
    _l_(553236)
    _c_(553239, _a_(553238, _n_(553237, "http", lambda: http), "serve_forever"))
    _l_(553240)