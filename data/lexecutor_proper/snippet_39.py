# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/332289/how-do-i-change-the-size-of-figures-drawn-with-matplotlib
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
fig = _c_(62791, _a_(62790, _a_(62789, _n_(62788, "matplotlib", lambda: matplotlib), "pyplot"), "gcf"))
_l_(62792)
_c_(62795, _a_(62794, _n_(62793, "fig", lambda: fig), "set_size_inches"), 18.5, 10.5)
_l_(62796)
_c_(62799, _a_(62798, _n_(62797, "fig", lambda: fig), "savefig"), 'test2png.png', dpi=100)
_l_(62800)

_c_(62803, _a_(62802, _n_(62801, "fig", lambda: fig), "set_size_inches"), 18.5, 10.5, forward=True)
_l_(62804)

_c_(62807, _a_(62806, _n_(62805, "fig", lambda: fig), "set_dpi"), 100)
_l_(62808)

