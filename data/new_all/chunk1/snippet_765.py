# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58882030/how-do-i-fix-this-attributeerror-subrequest-object-has-no-attribute-getfunca
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(404728, _a_(404727, _n_(404726, "pytest", lambda: pytest), "fixture"), autouse=True)
def _configure_application(request, monkeypatch):
    _l_(404733)

    """Use `pytest.mark.options` decorator to pass options to your application
    factory::

        @pytest.mark.options(debug=False)
        def test_something(app):
            assert not app.debug, 'the application works not in debug mode!'

    """
    if 'app' not in _a_(404730, _n_(404729, "request", lambda: request), "fixturenames"):
        _l_(404732)

        aux = ""
        _l_(404731)
        return aux