# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/11774265/how-do-you-access-the-query-string-in-flask-routes
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
date = _c_(63223, _a_(63222, _a_(63221, _n_(63220, "request", lambda: request), "args"), "get"), 'date')
_l_(63224)
try:
    from flask import request
    _l_(63226)

except ImportError:
    pass

