# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71716965/how-can-i-fix-this-attributeerror-module-numbers-has-no-attribute-integral
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(617367)

except ImportError:
    pass

fileobj = _c_(617369, _n_(617368, "open", lambda: open), 'marchweatherfull.csv', 'r')
_l_(617370)
data = _c_(617373, _a_(617372, _n_(617371, "fileobj", lambda: fileobj), "readlines"))
_l_(617374)
_c_(617377, _a_(617376, _n_(617375, "fileobj", lambda: fileobj), "close"))
_l_(617378)

mins = [] # do the same for maxs, nines and threes
_l_(617379) # do the same for maxs, nines and threes
maxs = []
_l_(617380)
nines = []
_l_(617381)
threes = []
_l_(617382)

for line in _n_(617383, "data", lambda: data):
    _l_(617416)

    splitline = _c_(617386, _a_(617385, _n_(617384, "line", lambda: line), "split"), ',')
    _l_(617387)
    _c_(617393, _a_(617389, _n_(617388, "mins", lambda: mins), "append"), _c_(617392, _n_(617390, "float", lambda: float), _n_(617391, "splitline", lambda: splitline)[2]))
    _l_(617394)
    _c_(617400, _a_(617396, _n_(617395, "maxs", lambda: maxs), "append"), _c_(617399, _n_(617397, "float", lambda: float), _n_(617398, "splitline", lambda: splitline)[3]))
    _l_(617401)
    _c_(617407, _a_(617403, _n_(617402, "nines", lambda: nines), "append"), _c_(617406, _n_(617404, "float", lambda: float), _n_(617405, "splitline", lambda: splitline)[10]))
    _l_(617408)
    _c_(617414, _a_(617410, _n_(617409, "threes", lambda: threes), "append"), _c_(617413, _n_(617411, "float", lambda: float), _n_(617412, "splitline", lambda: splitline)[16]))
    _l_(617415)

dates = [_n_(617417, "d", lambda: d) for d in _c_(617419, _n_(617418, "range", lambda: range), 1,32)]
_l_(617420)
_c_(617431, _a_(617422, _n_(617421, "plt", lambda: plt), "plot"), _n_(617423, "dates", lambda: dates), _n_(617424, "mins", lambda: mins), _n_(617425, "dates", lambda: dates), _n_(617426, "maxs", lambda: maxs), _n_(617427, "dates", lambda: dates), _n_(617428, "nines", lambda: nines), _n_(617429, "dates", lambda: dates), _n_(617430, "threes", lambda: threes))
_l_(617432)
_c_(617435, _a_(617434, _n_(617433, "plt", lambda: plt), "show"))
_l_(617436)


_c_(617439, _n_(617437, "print", lambda: print), _n_(617438, "mins", lambda: mins))
_l_(617440)