# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41653320/flask-socketio-split-app-py-attributeerror-blueprint-object-has-no-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from gevent import monkey
    _l_(442302)

except ImportError:
    pass
try:
    from flask import Flask, render_template, request
    _l_(442304)

except ImportError:
    pass
try:
    from flask_socketio import SocketIO
    _l_(442306)

except ImportError:
    pass
_c_(442309, _a_(442308, _n_(442307, "monkey", lambda: monkey), "patch_all"))
_l_(442310)


app = _c_(442313, _n_(442311, "Flask", lambda: Flask), _n_(442312, "__name__", lambda: __name__))
_l_(442314)
socketio = _c_(442317, _n_(442315, "SocketIO", lambda: SocketIO), _n_(442316, "app", lambda: app))
_l_(442318)


@_c_(442321, _a_(442320, _n_(442319, "app", lambda: app), "route"), '/')
def main():
    _l_(442325)

    aux = _c_(442323, _n_(442322, "render_template", lambda: render_template), 'main.html')
    _l_(442324)
    return aux



@_c_(442328, _a_(442327, _n_(442326, "socketio", lambda: socketio), "on"), 'connect', namespace='/dd')
def ws_conn():
    _l_(442333)

    _c_(442331, _a_(442330, _n_(442329, "socketio", lambda: socketio), "emit"), 'msg', {'count': 1}, namespace='/dd')
    _l_(442332)


@_c_(442336, _a_(442335, _n_(442334, "socketio", lambda: socketio), "on"), 'disconnect', namespace='/dd')
def ws_disconn():
    _l_(442340)

    _c_(442338, _n_(442337, "print", lambda: print), "Disconnected")
    _l_(442339)



if _n_(442341, "__name__", lambda: __name__) == '__main__':
    _l_(442347)

    _c_(442345, _a_(442343, _n_(442342, "socketio", lambda: socketio), "run"), _n_(442344, "app", lambda: app), "0.0.0.0", port=80)
    _l_(442346)