# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55063427/flask-blueprint-returns-nameerror-when-trying-to-register-blueprint-on-the-app-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from app import app
    _l_(352284)

except ImportError:
    pass

_n_(352285, "app", lambda: app).secret_key=_n_(352286, "flask_secret_key", lambda: flask_secret_key)
_l_(352287)

_c_(352291, _a_(352289, _n_(352288, "app", lambda: app), "run"), debug=_n_(352290, "debug", lambda: debug))
_l_(352292)