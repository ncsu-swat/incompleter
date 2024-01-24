# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41653320/flask-socketio-split-app-py-attributeerror-blueprint-object-has-no-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Blueprint, render_template, Flask
    _l_(449600)

except ImportError:
    pass
try:
    from flask_socketio import SocketIO
    _l_(449602)

except ImportError:
    pass
app = _c_(449605, _n_(449603, "Blueprint", lambda: Blueprint), 'app', _n_(449604, "__name__", lambda: __name__))
_l_(449606)

socketio = _c_(449609, _n_(449607, "SocketIO", lambda: SocketIO), _n_(449608, "app", lambda: app))
_l_(449610)


@_c_(449613, _a_(449612, _n_(449611, "app", lambda: app), "route"), '/')
def main():
    _l_(449617)

    aux = _c_(449615, _n_(449614, "render_template", lambda: render_template), 'main.html')
    _l_(449616)
    return aux


@_c_(449620, _a_(449619, _n_(449618, "socketio", lambda: socketio), "on"), 'connect', namespace='/dd')
def ws_conn():
    _l_(449628)

    _c_(449622, _n_(449621, "print", lambda: print), "connect")
    _l_(449623)
    _c_(449626, _a_(449625, _n_(449624, "socketio", lambda: socketio), "emit"), 'msg', {'count': 1}, namespace='/dd')
    _l_(449627)


@_c_(449631, _a_(449630, _n_(449629, "socketio", lambda: socketio), "on"), 'disconnect', namespace="/dd")
def ws_disconn():
    _l_(449635)

    _c_(449633, _n_(449632, "print", lambda: print), "disconnect")
    _l_(449634)