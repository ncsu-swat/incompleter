# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58631764/attribute-error-when-testing-flask-with-pytest-fixture
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
{...}
_l_(706362)

@_c_(706365, _a_(706364, _n_(706363, "pytest", lambda: pytest), "fixture"), scope='session', autouse=True)
def app(request):
    _l_(706389)

    app = _c_(706367, _n_(706366, "create_app", lambda: create_app), {
        'TESTING': True
    })
    _l_(706368)
    ctx = _c_(706371, _a_(706370, _n_(706369, "app", lambda: app), "app_context"))
    _l_(706372)
    _c_(706375, _a_(706374, _n_(706373, "ctx", lambda: ctx), "push"))
    _l_(706376)

    def teardown():
        _l_(706381)

        _c_(706379, _a_(706378, _n_(706377, "ctx", lambda: ctx), "pop"))
        _l_(706380)

    _c_(706385, _a_(706383, _n_(706382, "request", lambda: request), "addfinalizer"), _n_(706384, "teardown", lambda: teardown))
    _l_(706386)
    aux = _n_(706387, "app", lambda: app)
    _l_(706388)
    return aux

@_c_(706392, _a_(706391, _n_(706390, "pytest", lambda: pytest), "fixture"), scope='function')
def client(app, request):
    _l_(706397)

    aux = _c_(706395, _a_(706394, _n_(706393, "app", lambda: app), "test_client"))
    _l_(706396)
    return aux

@_c_(706400, _a_(706399, _n_(706398, "pytest", lambda: pytest), "fixture"), scope='function')
def get(client):
    _l_(706406)

    aux = _c_(706404, _n_(706401, "humanize_werkzeug_client", lambda: humanize_werkzeug_client), _a_(706403, _n_(706402, "client", lambda: client), "get"))
    _l_(706405)
    return aux