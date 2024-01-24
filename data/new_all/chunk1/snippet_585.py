# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69636611/attributeerror-super-object-has-no-attribute-word-weighting
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class FLSA(_n_(398581, "FTM", lambda: FTM)):
    _l_(398595)

    def __init__(self, word_weighting='normal'):
        _l_(398594)

        _c_(398585, _a_(398583, _n_(398582, "super", lambda: super)(), "__init__"), word_weighting = _n_(398584, "word_weighting", lambda: word_weighting))
        _l_(398586)
        _n_(398587, "self", lambda: self).sparse_global_term_weighting = _c_(398592, _a_(398589, _n_(398588, "super", lambda: super)(), "get_sparse_global_term_weights"), word_weighting = _a_(398591, _n_(398590, "super", lambda: super)(), "word_weighting"))
        _l_(398593)