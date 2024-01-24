# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71716965/how-can-i-fix-this-attributeerror-module-numbers-has-no-attribute-integral
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(639862)

except ImportError:
    pass

fileobj = _c_(639864, _n_(639863, "open", lambda: open), 'marchweatherfull.csv', 'r')
_l_(639865)
data = _c_(639868, _a_(639867, _n_(639866, "fileobj", lambda: fileobj), "readlines"))
_l_(639869)
_c_(639872, _a_(639871, _n_(639870, "fileobj", lambda: fileobj), "close"))
_l_(639873)

mins = [] # do the same for maxs, nines and threes
_l_(639874) # do the same for maxs, nines and threes
maxs = []
_l_(639875)
nines = []
_l_(639876)
threes = []
_l_(639877)

for line in _n_(639878, "data", lambda: data):
    _l_(639911)

    splitline = _c_(639881, _a_(639880, _n_(639879, "line", lambda: line), "split"), ',')
    _l_(639882)
    _c_(639888, _a_(639884, _n_(639883, "mins", lambda: mins), "append"), _c_(639887, _n_(639885, "float", lambda: float), _n_(639886, "splitline", lambda: splitline)[2]))
    _l_(639889)
    _c_(639895, _a_(639891, _n_(639890, "maxs", lambda: maxs), "append"), _c_(639894, _n_(639892, "float", lambda: float), _n_(639893, "splitline", lambda: splitline)[3]))
    _l_(639896)
    _c_(639902, _a_(639898, _n_(639897, "nines", lambda: nines), "append"), _c_(639901, _n_(639899, "float", lambda: float), _n_(639900, "splitline", lambda: splitline)[10]))
    _l_(639903)
    _c_(639909, _a_(639905, _n_(639904, "threes", lambda: threes), "append"), _c_(639908, _n_(639906, "float", lambda: float), _n_(639907, "splitline", lambda: splitline)[16]))
    _l_(639910)

dates = [_n_(639912, "d", lambda: d) for d in _c_(639914, _n_(639913, "range", lambda: range), 1,32)]
_l_(639915)
_c_(639926, _a_(639917, _n_(639916, "plt", lambda: plt), "plot"), _n_(639918, "dates", lambda: dates), _n_(639919, "mins", lambda: mins), _n_(639920, "dates", lambda: dates), _n_(639921, "maxs", lambda: maxs), _n_(639922, "dates", lambda: dates), _n_(639923, "nines", lambda: nines), _n_(639924, "dates", lambda: dates), _n_(639925, "threes", lambda: threes))
_l_(639927)
_c_(639930, _a_(639929, _n_(639928, "plt", lambda: plt), "show"))
_l_(639931)


_c_(639934, _n_(639932, "print", lambda: print), _n_(639933, "mins", lambda: mins))
_l_(639935)