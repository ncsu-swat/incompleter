# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52626178/sessions-in-web-py-causing-nameerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
app = _c_(672972, _a_(672968, _n_(672967, "web", lambda: web), "application"), _n_(672969, "urls", lambda: urls), _c_(672971, _n_(672970, "globals", lambda: globals)))
_l_(672973)
# Session
session = _c_(672982, _a_(672976, _a_(672975, _n_(672974, "web", lambda: web), "session"), "Session"), _n_(672977, "app", lambda: app), _c_(672981, _a_(672980, _a_(672979, _n_(672978, "web", lambda: web), "session"), "DiskStore"), "sessions"), initializer={'user': 'none'})
_l_(672983)
session_data = _a_(672985, _n_(672984, "session", lambda: session), "_initializer")
_l_(672986)

render = _c_(672992, _a_(672989, _a_(672988, _n_(672987, "web", lambda: web), "template"), "render"), "Views/Templates", base="MainLayout", globals={'session': _n_(672990, "session_data", lambda: session_data), 'current_user': _n_(672991, "session_data", lambda: session_data)['user']})
_l_(672993)