# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65012433/identifying-location-of-error-typeerror-nonetype-object-is-not-subscriptable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask, request, jsonify
    _l_(412481)

except ImportError:
    pass
try:
    from Service import ToDoService
    _l_(412483)

except ImportError:
    pass
try:
    from models import Schema
    _l_(412485)

except ImportError:
    pass

app = _c_(412488, _n_(412486, "Flask", lambda: Flask), _n_(412487, "__name__", lambda: __name__))
_l_(412489)

@_c_(412492, _a_(412491, _n_(412490, "app", lambda: app), "route"), "/todo", methods=["GET", "POST"])
def create_todo():
    _l_(412503)

    aux = _c_(412501, _n_(412493, "jsonify", lambda: jsonify), _c_(412500, _a_(412496, _c_(412495, _n_(412494, "ToDoService", lambda: ToDoService)), "create"), _c_(412499, _a_(412498, _n_(412497, "request", lambda: request), "get_json"))))
    _l_(412502)
    return aux

if _n_(412504, "__name__", lambda: __name__) == "__main__":
    _l_(412512)

    _c_(412506, _n_(412505, "Schema", lambda: Schema))
    _l_(412507)
    _c_(412510, _a_(412509, _n_(412508, "app", lambda: app), "run"), debug=True)
    _l_(412511)