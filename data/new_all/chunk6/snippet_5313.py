# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69930885/typeerror-module-object-is-not-callable-py-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import flask
    _l_(348246)

except ImportError:
    pass
try:
    import _thread
    _l_(348248)

except ImportError:
    pass

app = _c_(348251, _a_(348250, _n_(348249, "flask", lambda: flask), "Flask"), 'Keep Alive')
_l_(348252)

@_c_(348255, _a_(348254, _n_(348253, "app", lambda: app), "route"), '/')
def home():
    _l_(348257)

    aux = "I'm alive"
    _l_(348256)
    return aux

def run():
    _l_(348262)

    _c_(348260, _a_(348259, _n_(348258, "app", lambda: app), "run"), host='0.0.0.0',port=8080)
    _l_(348261)

def keep_alive():
    _l_(348271)

    t = _c_(348265, _n_(348263, "_thread", lambda: _thread), target=_n_(348264, "run", lambda: run))
    _l_(348266)
    _c_(348269, _a_(348268, _n_(348267, "t", lambda: t), "start"))
    _l_(348270)