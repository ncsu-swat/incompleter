# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/16778961/attributeerror-map-object-has-no-attribute-extend-in-matplotlib-setup
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Extension(_n_(557523, "_Extension", lambda: _Extension)):
    _l_(557557)

    """Extension that uses '.c' files in place of '.pyx' files"""

    def __init__(self, *args, **kw):
        _l_(557538)

        _c_(557529, _a_(557525, _n_(557524, "_Extension", lambda: _Extension), "__init__"), _n_(557526, "self", lambda: self), *_n_(557527, "args", lambda: args), **_n_(557528, "kw", lambda: kw))
        _l_(557530)
        if not _c_(557532, _n_(557531, "have_pyrex", lambda: have_pyrex)):
            _l_(557537)

            _c_(557535, _a_(557534, _n_(557533, "self", lambda: self), "_convert_pyx_sources_to_c"))
            _l_(557536)

    def _convert_pyx_sources_to_c(self):
        _l_(557556)

        "convert .pyx extensions to .c"
        _l_(557539)
        def pyx_to_c(source):
            _l_(557548)

            if _c_(557542, _a_(557541, _n_(557540, "source", lambda: source), "endswith"), '.pyx'):
                _l_(557545)

                source = _n_(557543, "source", lambda: source)[:-4] + '.c'
                _l_(557544)
            aux = _n_(557546, "source", lambda: source)
            _l_(557547)
            return aux
        _n_(557549, "self", lambda: self).sources = _c_(557554, _n_(557550, "map", lambda: map), _n_(557551, "pyx_to_c", lambda: pyx_to_c), _a_(557553, _n_(557552, "self", lambda: self), "sources"))
        _l_(557555)