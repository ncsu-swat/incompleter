# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51654811/attributeerror-turtle-object-has-no-attribute-pencolour
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import turtle
    _l_(360715)

except ImportError:
    pass

t = _c_(360718, _a_(360717, _n_(360716, "turtle", lambda: turtle), "Pen"))    
_l_(360719)    
_c_(360722, _a_(360721, _n_(360720, "t", lambda: t), "speed"), 0)
_l_(360723)
colours = ["green", "blue", "dark purple", "grey"]
_l_(360724)

for x in _c_(360726, _n_(360725, "range", lambda: range), 100):
    _l_(360742)

    _c_(360731, _a_(360728, _n_(360727, "t", lambda: t), "pencolour"), _n_(360729, "colours", lambda: colours)[ _n_(360730, "x", lambda: x) % 4] )
    _l_(360732)
    _c_(360736, _a_(360734, _n_(360733, "t", lambda: t), "cirlce"), 2*_n_(360735, "x", lambda: x))
    _l_(360737)
    _c_(360740, _a_(360739, _n_(360738, "t", lambda: t), "left"), 91)
    _l_(360741)