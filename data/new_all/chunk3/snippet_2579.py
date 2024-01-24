# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70885979/trying-to-test-flask-endpoint-attributeerror-posixpath-object-has-no-attribu
# conftest.py

# ... imports here ...

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_a_(523790, _n_(523789, "pytest", lambda: pytest), "fixture")
def client():
    _l_(523820)

    _c_(523795, _a_(523793, _a_(523792, _n_(523791, "app", lambda: app), "config"), "from_object"), _n_(523794, "TestSettings", lambda: TestSettings))
    _l_(523796)
    with _c_(523799, _a_(523798, _n_(523797, "app", lambda: app), "test_client")) as client:
        _l_(523819)

        with _c_(523802, _a_(523801, _n_(523800, "app", lambda: app), "app_context")):
            _l_(523807)

            # starts connection with tests db
            db = _c_(523805, _n_(523803, "MongoEngine", lambda: MongoEngine), _n_(523804, "app", lambda: app))
            _l_(523806)

        yield _n_(523808, "client", lambda: client)  # Do the tests
        _l_(523809)  # Do the tests

        with _c_(523812, _a_(523811, _n_(523810, "app", lambda: app), "app_context")):
            _l_(523818)

            # drop db after tests
            _c_(523816, _a_(523815, _a_(523814, _n_(523813, "db", lambda: db), "connection"), "drop_database"), 'test')
            _l_(523817)