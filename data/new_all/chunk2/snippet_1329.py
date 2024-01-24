# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41653320/flask-socketio-split-app-py-attributeerror-blueprint-object-has-no-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from gevent import monkey
    _l_(428236)

except ImportError:
    pass
try:
    from flask import Flask, render_template, request
    _l_(428238)

except ImportError:
    pass
try:
    from flask_socketio import SocketIO
    _l_(428240)

except ImportError:
    pass
_c_(428243, _a_(428242, _n_(428241, "monkey", lambda: monkey), "patch_all"))
_l_(428244)
try:
    from App.views import test
    _l_(428246)

except ImportError:
    pass
app = _c_(428249, _n_(428247, "Flask", lambda: Flask), _n_(428248, "__name__", lambda: __name__), template_folder='app/templates')
_l_(428250)
_c_(428255, _a_(428252, _n_(428251, "app", lambda: app), "register_blueprint"), _a_(428254, _n_(428253, "test", lambda: test), "app"))
_l_(428256)
socketio = _c_(428259, _n_(428257, "SocketIO", lambda: SocketIO), _n_(428258, "app", lambda: app))
_l_(428260)

if _n_(428261, "__name__", lambda: __name__) == '__main__':
    _l_(428267)

    _c_(428265, _a_(428263, _n_(428262, "socketio", lambda: socketio), "run"), _n_(428264, "app", lambda: app), "0.0.0.0", port=80)
    _l_(428266)