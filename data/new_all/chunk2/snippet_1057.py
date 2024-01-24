# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48492332/flask-peewee-error-attributeerror-flask-object-has-no-attribute-compiler
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from comparteme import app
    _l_(454900)

except ImportError:
    pass
try:
    from comparteme.models.base_model import User
    _l_(454902)

except ImportError:
    pass


@_c_(454905, _a_(454904, _n_(454903, "app", lambda: app), "route"), '/')
@_c_(454908, _a_(454907, _n_(454906, "app", lambda: app), "route"), '/index')
def index():
    _l_(454914)

    _c_(454911, _a_(454910, _n_(454909, "User", lambda: User), "create"), username='Alan')
    _l_(454912)
    aux = 'returning any string'
    _l_(454913)
    return aux