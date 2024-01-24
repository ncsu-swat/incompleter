# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52008881/flask-attributeerror-blueprint-object-has-no-attribute-response-class
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask
    _l_(453165)

except ImportError:
    pass

...
_l_(453166)
app = _c_(453169, _n_(453167, "Flask", lambda: Flask), _n_(453168, "__name__", lambda: __name__))
_l_(453170)

...
_l_(453171)
...
_l_(453172)
try:
    from my_app.auth.views import bp
    _l_(453174)

except ImportError:
    pass
_c_(453178, _a_(453176, _n_(453175, "app", lambda: app), "register_blueprint"), _n_(453177, "bp", lambda: bp))
_l_(453179)