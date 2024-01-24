# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43274942/falcon-attributeerror-api-object-has-no-attribute-create
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from falcon import testing
    _l_(383253)

except ImportError:
    pass
try:
    import pytest
    _l_(383255)

except ImportError:
    pass
try:
    from app import api
    _l_(383257)

except ImportError:
    pass


@_c_(383260, _a_(383259, _n_(383258, "pytest", lambda: pytest), "fixture"), scope='module')
def client():
    _l_(383268)

    aux = _c_(383266, _a_(383262, _n_(383261, "testing", lambda: testing), "TestClient"), _c_(383265, _a_(383264, _n_(383263, "api", lambda: api), "create")))
    _l_(383267)
    # Assume the hypothetical `myapp` package has a
    # function called `create()` to initialize and
    # return a `falcon.API` instance.
    return aux


def test_get_message(client):
    _l_(383276)

    result = _c_(383271, _a_(383270, _n_(383269, "client", lambda: client), "simulate_get"), '/')
    _l_(383272)
    assert _a_(383274, _n_(383273, "result", lambda: result), "status_code") == 200
    _l_(383275)