# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59012381/pytest-flask-application-attributeerror-module-src-api-has-no-attribute-test
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pytest
    _l_(379302)

except ImportError:
    pass
try:
    from src import api
    _l_(379304)

except ImportError:
    pass


_n_(379305, "api", lambda: api).testing = True
_l_(379306)
client = _c_(379309, _a_(379308, _n_(379307, "api", lambda: api), "test_client"))
_l_(379310)


def test_route(client):
    _l_(379318)

    response = _c_(379313, _a_(379312, _n_(379311, "api", lambda: api), "get"), '/')
    _l_(379314)
    assert _a_(379316, _n_(379315, "response", lambda: response), "status_code") == 200
    _l_(379317)