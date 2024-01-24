# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/16778961/attributeerror-map-object-has-no-attribute-extend-in-matplotlib-setup
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Extension(_n_(563207, "_Extension", lambda: _Extension)):
    _l_(563238)

    """Extension that uses '.c' files in place of '.pyx' files"""

    if not have_pyrex:
        _l_(563237)

        # convert .pyx extensions to .c 
        def __init__(self,*args,**kw):
            _l_(563236)

            _c_(563213, _a_(563209, _n_(563208, "_Extension", lambda: _Extension), "__init__"), _n_(563210, "self", lambda: self),*_n_(563211, "args", lambda: args),**_n_(563212, "kw", lambda: kw))
            _l_(563214)
            sources = []
            _l_(563215)
            for s in _a_(563217, _n_(563216, "self", lambda: self), "sources"):
                _l_(563232)

                if _c_(563220, _a_(563219, _n_(563218, "s", lambda: s), "endswith"), '.pyx'):
                    _l_(563231)

                    _c_(563224, _a_(563222, _n_(563221, "sources", lambda: sources), "append"), _n_(563223, "s", lambda: s)[:-3]+'c')
                    _l_(563225)
                else:
                    _c_(563229, _a_(563227, _n_(563226, "sources", lambda: sources), "append"), _n_(563228, "s", lambda: s))
                    _l_(563230)
            _n_(563233, "self", lambda: self).sources = _n_(563234, "sources", lambda: sources)
            _l_(563235)