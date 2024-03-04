# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2077897/substitute-multiple-whitespace-with-single-whitespace-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(64213)

except ImportError:
    pass

_RE_COMBINE_WHITESPACE = _c_(64216, _a_(64215, _n_(64214, "re", lambda: re), "compile"), r"\s+")
_l_(64217)

my_str = _c_(64223, _a_(64222, _c_(64221, _a_(64219, _n_(64218, "_RE_COMBINE_WHITESPACE", lambda: _RE_COMBINE_WHITESPACE), "sub"), " ", _n_(64220, "my_str", lambda: my_str)), "strip"))
_l_(64224)
try:
    import re
    _l_(64226)

except ImportError:
    pass

_RE_COMBINE_WHITESPACE = _c_(64229, _a_(64228, _n_(64227, "re", lambda: re), "compile"), r"(?a:\s+)")
_l_(64230)
_RE_STRIP_WHITESPACE = _c_(64233, _a_(64232, _n_(64231, "re", lambda: re), "compile"), r"(?a:^\s+|\s+$)")
_l_(64234)

my_str = _c_(64238, _a_(64236, _n_(64235, "_RE_COMBINE_WHITESPACE", lambda: _RE_COMBINE_WHITESPACE), "sub"), " ", _n_(64237, "my_str", lambda: my_str))
_l_(64239)
my_str = _c_(64243, _a_(64241, _n_(64240, "_RE_STRIP_WHITESPACE", lambda: _RE_STRIP_WHITESPACE), "sub"), "", _n_(64242, "my_str", lambda: my_str))
_l_(64244)

