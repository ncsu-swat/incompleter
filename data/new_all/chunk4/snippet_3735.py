# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68942337/typeerror-only-size-1-arrays-can-be-converted-to-python-scalars-with-a-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
x=[0,1,2]
_l_(590993)
y=_c_(590996, _a_(590995, _n_(590994, "np", lambda: np), "linspace"), 69,420,69420)
_l_(590997)
X, Y = _c_(591002, _a_(590999, _n_(590998, "np", lambda: np), "meshgrid"), _n_(591000, "x", lambda: x), _n_(591001, "y", lambda: y))
_l_(591003)

fig, axs = _c_(591006, _a_(591005, _n_(591004, "plt", lambda: plt), "subplots"))
_l_(591007)
_c_(591016, _a_(591009, _n_(591008, "axs", lambda: axs), "contour"), _n_(591010, "X", lambda: X),_n_(591011, "Y", lambda: Y),_c_(591015, _n_(591012, "G", lambda: G), _n_(591013, "X", lambda: X),_n_(591014, "Y", lambda: Y)),levels=[420.69],colors='black')
_l_(591017)