# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/38044773/receiving-typeerror-object-new-takes-no-parameters-when-new-not-chang
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from random import randint
    _l_(448919)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(448921)

except ImportError:
    pass

class Cell:
    _l_(448973)

    def __init__(self, master, state=None):
        _l_(448943)

        if _n_(448922, "state", lambda: state) is None:
            _l_(448926)

            state = _c_(448924, _n_(448923, "randint", lambda: randint), 0,2)
            _l_(448925)
        _n_(448927, "self", lambda: self).state = _n_(448928, "state", lambda: state)
        _l_(448929)
        _n_(448930, "self", lambda: self).next_state = _n_(448931, "state", lambda: state)
        _l_(448932)
        _n_(448933, "self", lambda: self).button = _c_(448941, _a_(448939, _c_(448938, _n_(448934, "Button", lambda: Button), _n_(448935, "master", lambda: master), width=2, height=1, bg = 'black' if _a_(448937, _n_(448936, "self", lambda: self), "state") == 1 else 'white'), "pack"), side=_n_(448940, "LEFT", lambda: LEFT))
        _l_(448942)

    def __del__(self):
        _l_(448949)

        _c_(448947, _a_(448946, _a_(448945, _n_(448944, "self", lambda: self), "button"), "destroy"))
        _l_(448948)

    def set_next_state(self, neighbours):
        _l_(448960)

        if _a_(448951, _n_(448950, "self", lambda: self), "state") == 1:
            _l_(448959)

            _n_(448952, "self", lambda: self).next_state = 0 if _n_(448953, "neighbours", lambda: neighbours) < 2 or _n_(448954, "neighbours", lambda: neighbours) > 3 else 1
            _l_(448955)
        else:
            _n_(448956, "self", lambda: self).next_state = 1 if _n_(448957, "neighbours", lambda: neighbours) == 3 else 0
            _l_(448958)

    def update(self):
        _l_(448972)

        _n_(448961, "self", lambda: self).state = _a_(448963, _n_(448962, "self", lambda: self), "next_state")
        _l_(448964)
        _c_(448970, _a_(448967, _a_(448966, _n_(448965, "self", lambda: self), "button"), "config"), bg = 'black' if _a_(448969, _n_(448968, "self", lambda: self), "state") == 1 else 'white')
        _l_(448971)