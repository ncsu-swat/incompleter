# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58631764/attribute-error-when-testing-flask-with-pytest-fixture
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
{...}
_l_(698713)

@_c_(698716, _a_(698715, _n_(698714, "pytest", lambda: pytest), "fixture"), scope='session', autouse=True)
def app(request):
    _l_(698740)

    app = _c_(698718, _n_(698717, "create_app", lambda: create_app), {
        'TESTING': True
    })
    _l_(698719)
    ctx = _c_(698722, _a_(698721, _n_(698720, "app", lambda: app), "app_context"))
    _l_(698723)
    _c_(698726, _a_(698725, _n_(698724, "ctx", lambda: ctx), "push"))
    _l_(698727)

    def teardown():
        _l_(698732)

        _c_(698730, _a_(698729, _n_(698728, "ctx", lambda: ctx), "pop"))
        _l_(698731)

    _c_(698736, _a_(698734, _n_(698733, "request", lambda: request), "addfinalizer"), _n_(698735, "teardown", lambda: teardown))
    _l_(698737)
    aux = _n_(698738, "app", lambda: app)
    _l_(698739)
    return aux

@_c_(698743, _a_(698742, _n_(698741, "pytest", lambda: pytest), "fixture"), scope='function')
def client(app, request):
    _l_(698748)

    aux = _c_(698746, _a_(698745, _n_(698744, "app", lambda: app), "test_client"))
    _l_(698747)
    return aux

@_c_(698751, _a_(698750, _n_(698749, "pytest", lambda: pytest), "fixture"), scope='function')
def get(client):
    _l_(698757)

    aux = _c_(698755, _n_(698752, "humanize_werkzeug_client", lambda: humanize_werkzeug_client), _a_(698754, _n_(698753, "client", lambda: client), "get"))
    _l_(698756)
    return aux