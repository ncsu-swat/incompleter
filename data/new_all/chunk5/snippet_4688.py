# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52626178/sessions-in-web-py-causing-nameerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
app = _c_(649301, _a_(649297, _n_(649296, "web", lambda: web), "application"), _n_(649298, "urls", lambda: urls), _c_(649300, _n_(649299, "globals", lambda: globals)))
_l_(649302)
# Session
session = _c_(649311, _a_(649305, _a_(649304, _n_(649303, "web", lambda: web), "session"), "Session"), _n_(649306, "app", lambda: app), _c_(649310, _a_(649309, _a_(649308, _n_(649307, "web", lambda: web), "session"), "DiskStore"), "sessions"), initializer={'user': 'none'})
_l_(649312)
session_data = _a_(649314, _n_(649313, "session", lambda: session), "_initializer")
_l_(649315)

render = _c_(649321, _a_(649318, _a_(649317, _n_(649316, "web", lambda: web), "template"), "render"), "Views/Templates", base="MainLayout", globals={'session': _n_(649319, "session_data", lambda: session_data), 'current_user': _n_(649320, "session_data", lambda: session_data)['user']})
_l_(649322)