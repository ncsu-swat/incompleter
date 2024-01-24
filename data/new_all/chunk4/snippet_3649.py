# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70706978/loginmanager-typeerror-nonetype-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from website import create_app
    _l_(625898)

except ImportError:
    pass

app=_c_(625900, _n_(625899, "create_app", lambda: create_app))
_l_(625901)

if _n_(625902, "__name__", lambda: __name__)=='__main__':
    _l_(625907)

    _c_(625905, _a_(625904, _n_(625903, "app", lambda: app), "run"), host='0.0.0.0',port=80,debug=True)
    _l_(625906)