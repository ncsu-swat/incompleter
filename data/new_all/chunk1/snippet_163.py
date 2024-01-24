# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/35367340/importing-module-causes-typeerror-module-init-takes-at-most-2-arguments
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from actions import ListitAction
    _l_(383601)

except ImportError:
    pass

class ViewAction(_n_(383602, "ListitAction", lambda: ListitAction)):
    _l_(383614)


    def __init__(self, view_id):
        _l_(383611)

        _c_(383606, _a_(383604, _n_(383603, "ListitAction", lambda: ListitAction), "__init__"), _n_(383605, "self", lambda: self))
        _l_(383607)
        _n_(383608, "self", lambda: self).view_id = _n_(383609, "view_id", lambda: view_id)
        _l_(383610)

    def build_uri():
        _l_(383613)

        aux = "test"
        _l_(383612)
        return aux