# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72699297/python-flask-typeerror-not-supported-between-instances-of-nonetype-and
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask, request, session
    _l_(455392)

except ImportError:
    pass
try:
    from flask_session import Session
    _l_(455394)

except ImportError:
    pass
try:
    from functools import wraps
    _l_(455396)

except ImportError:
    pass
try:
    from datetime import timedelta
    _l_(455398)

except ImportError:
    pass
try:
    from json import dumps
    _l_(455400)

except ImportError:
    pass
try:
    from rest.api import api, users_api, setups_api, reports
    _l_(455402)

except ImportError:
    pass
try:
    import os
    _l_(455404)

except ImportError:
    pass
try:
    import shutil
    _l_(455406)

except ImportError:
    pass


# App Instance
app = _c_(455409, _n_(455407, "Flask", lambda: Flask), _n_(455408, "__name__", lambda: __name__))
_l_(455410)
project_path = _c_(455414, _a_(455413, _a_(455412, _n_(455411, "os", lambda: os), "path"), "abspath"), '.')
_l_(455415)
_a_(455417, _n_(455416, "app", lambda: app), "config")['APPLICATION_ROOT'] = _n_(455418, "project_path", lambda: project_path)
_l_(455419)
_a_(455421, _n_(455420, "app", lambda: app), "config")['SESSION_COOKIE_PATH'] = _n_(455422, "project_path", lambda: project_path) + "/cookies/"
_l_(455423)
_a_(455425, _n_(455424, "app", lambda: app), "config")['SESSION_TYPE'] = 'filesystem'
_l_(455426)
_c_(455429, _n_(455427, "Session", lambda: Session), _n_(455428, "app", lambda: app))
_l_(455430)


@_a_(455432, _n_(455431, "app", lambda: app), "before_request")
def make_session_permanent():
    _l_(455445)

    _n_(455433, "app", lambda: app).permanent_session_lifetime = _c_(455435, _n_(455434, "timedelta", lambda: timedelta), hours=(5))
    _l_(455436)
    if _a_(455438, _n_(455437, "request", lambda: request), "path") not in ["/api/login", "/api/get-session-data"]:
        _l_(455444)

        if not _c_(455441, _a_(455440, _n_(455439, "session", lambda: session), "get"), 'user'):
            _l_(455443)

            aux = "Sign in needed.", 403
            _l_(455442)
            return aux


@_c_(455448, _a_(455447, _n_(455446, "app", lambda: app), "route"), "/api/login", methods=["POST", ])
def login():
    _l_(455454)

    # login things
    _n_(455449, "session", lambda: session)['user'] = "whatever"
    _l_(455450)
    aux = _c_(455452, _n_(455451, "dumps", lambda: dumps), "")
    _l_(455453)
    return aux


@_c_(455457, _a_(455456, _n_(455455, "app", lambda: app), "route"), "/api/get-session-data")
def give_session_data():
    _l_(455466)

    session_data = {
        "user": _c_(455460, _a_(455459, _n_(455458, "session", lambda: session), "get"), "user")
    }
    _l_(455461)
    aux = _c_(455464, _n_(455462, "dumps", lambda: dumps), _n_(455463, "session_data", lambda: session_data))
    _l_(455465)
    return aux