# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/24988448/how-to-draw-vertical-lines-on-a-given-plot
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(1544470)

except ImportError:
    pass

# x coordinates for the lines
xcoords = [0.1, 0.3, 0.5]
_l_(1544471)
# colors for the lines
colors = ['r','k','b']
_l_(1544472)

for xc,c in _c_(1544476, _n_(1544473, "zip", lambda: zip), _n_(1544474, "xcoords", lambda: xcoords),_n_(1544475, "colors", lambda: colors)):
    _l_(1544486)

    _c_(1544484, _a_(1544478, _n_(1544477, "plt", lambda: plt), "axvline"), x=_n_(1544479, "xc", lambda: xc), label=_c_(1544482, _a_(1544480, 'line at x = {}', "format"), _n_(1544481, "xc", lambda: xc)), c=_n_(1544483, "c", lambda: c))
    _l_(1544485)

_c_(1544489, _a_(1544488, _n_(1544487, "plt", lambda: plt), "legend"))
_l_(1544490)
_c_(1544493, _a_(1544492, _n_(1544491, "plt", lambda: plt), "show"))
_l_(1544494)

