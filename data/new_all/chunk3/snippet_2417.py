# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43858513/pytest-typeerror-init-got-an-unexpected-keyword-argument-browser
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pytest
    _l_(534984)

except ImportError:
    pass
try:
    from fixture.application import Application
    _l_(534986)

except ImportError:
    pass
__author__ = 'Max'
_l_(534987)

fixture = None
_l_(534988)

@_a_(534990, _n_(534989, "pytest", lambda: pytest), "fixture")
def app(request):
    _l_(535017)

    global fixture
    _l_(534991)
    browser = _c_(534995, _a_(534994, _a_(534993, _n_(534992, "request", lambda: request), "config"), "getoption"), "--browser")
    _l_(534996)
    if _n_(534997, "fixture", lambda: fixture) is None:
        _l_(535009)

        fixture = _c_(535000, _n_(534998, "Application", lambda: Application), browser=_n_(534999, "browser", lambda: browser))
        _l_(535001)
    else:
        if not _a_(535003, _n_(535002, "fixture", lambda: fixture), "is_valid"):
            _l_(535008)

            fixture = _c_(535006, _n_(535004, "Application", lambda: Application), browser=_n_(535005, "browser", lambda: browser))
            _l_(535007)
    _c_(535013, _a_(535012, _a_(535011, _n_(535010, "fixture", lambda: fixture), "session"), "ensure_login"), username="somename", password="somepassword")
    _l_(535014)
    aux = _n_(535015, "fixture", lambda: fixture)
    _l_(535016)
    return aux

def pytest_addoption(parser):
    _l_(535022)

    # hooks for browsers
    _c_(535020, _a_(535019, _n_(535018, "parser", lambda: parser), "addoption"), "--browser", action="store", default="chrome")
    _l_(535021)