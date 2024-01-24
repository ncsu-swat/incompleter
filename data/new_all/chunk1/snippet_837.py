# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65012433/identifying-location-of-error-typeerror-nonetype-object-is-not-subscriptable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from models import ToDoModel
    _l_(404802)

except ImportError:
    pass


class ToDoService:
    _l_(404816)

    def __init__(self):
        _l_(404807)

        _n_(404803, "self", lambda: self).model = _c_(404805, _n_(404804, "ToDoModel", lambda: ToDoModel))
        _l_(404806)

    def create(self, params):
        _l_(404815)

        _c_(404813, _a_(404810, _a_(404809, _n_(404808, "self", lambda: self), "model"), "create"), _n_(404811, "params", lambda: params)["Title"], _n_(404812, "params", lambda: params)["Description"])
        _l_(404814)