# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58631764/attribute-error-when-testing-flask-with-pytest-fixture
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
{...}
_l_(692184)

@_c_(692187, _a_(692186, _n_(692185, "pytest", lambda: pytest), "fixture"), scope='session', autouse=True)
def app(request):
    _l_(692211)

    app = _c_(692189, _n_(692188, "create_app", lambda: create_app), {
        'TESTING': True
    })
    _l_(692190)
    ctx = _c_(692193, _a_(692192, _n_(692191, "app", lambda: app), "app_context"))
    _l_(692194)
    _c_(692197, _a_(692196, _n_(692195, "ctx", lambda: ctx), "push"))
    _l_(692198)

    def teardown():
        _l_(692203)

        _c_(692201, _a_(692200, _n_(692199, "ctx", lambda: ctx), "pop"))
        _l_(692202)

    _c_(692207, _a_(692205, _n_(692204, "request", lambda: request), "addfinalizer"), _n_(692206, "teardown", lambda: teardown))
    _l_(692208)
    aux = _n_(692209, "app", lambda: app)
    _l_(692210)
    return aux

@_c_(692214, _a_(692213, _n_(692212, "pytest", lambda: pytest), "fixture"), scope='function')
def client(app, request):
    _l_(692219)

    aux = _c_(692217, _a_(692216, _n_(692215, "app", lambda: app), "test_client"))
    _l_(692218)
    return aux

@_c_(692222, _a_(692221, _n_(692220, "pytest", lambda: pytest), "fixture"), scope='function')
def get(client):
    _l_(692228)

    aux = _c_(692226, _n_(692223, "humanize_werkzeug_client", lambda: humanize_werkzeug_client), _a_(692225, _n_(692224, "client", lambda: client), "get"))
    _l_(692227)
    return aux