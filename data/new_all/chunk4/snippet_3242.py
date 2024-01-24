# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76844263/flaskapi-attributeerror-module-app-routers-api-has-no-attribute-register
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Blueprint, request
    _l_(601644)

except ImportError:
    pass
try:
    from app.models import User
    _l_(601646)

except ImportError:
    pass
try:
    from app.db import get_db
    _l_(601648)

except ImportError:
    pass


bp = _c_(601651, _n_(601649, "Blueprint", lambda: Blueprint), 'api', _n_(601650, "__name__", lambda: __name__), url_prefix = '/api')
_l_(601652)

@_c_(601655, _a_(601654, _n_(601653, "bp", lambda: bp), "route"), '/users', methods = ['POST'])
def signup():
    _l_(601665)

    data = _c_(601658, _a_(601657, _n_(601656, "request", lambda: request), "get_json"))
    _l_(601659)
    _c_(601662, _n_(601660, "print", lambda: print), _n_(601661, "data", lambda: data))
    _l_(601663)
    aux = ''
    _l_(601664)
    return aux