# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63981530/i-get-typeerror-cant-multiply-sequence-by-non-int-of-type-numpy-float64-when
# This is my code that creates the plot
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
moving_avg = _c_(337854, _a_(337849, _n_(337848, "np", lambda: np), "convolve"), _n_(337850, "list_of_results", lambda: list_of_results), _c_(337853, _a_(337852, _n_(337851, "np", lambda: np), "ones"), (100,)) / 100, mode="valid")
_l_(337855)
_c_(337865, _a_(337857, _n_(337856, "plt", lambda: plt), "plot"), [_n_(337858, "i", lambda: i) for i in _c_(337863, _n_(337859, "range", lambda: range), _c_(337862, _n_(337860, "len", lambda: len), _n_(337861, "moving_avg", lambda: moving_avg)))], _n_(337864, "moving_avg", lambda: moving_avg))
_l_(337866)
_c_(337869, _a_(337868, _n_(337867, "plt", lambda: plt), "ylabel"), 'Remaining Pins')
_l_(337870)
_c_(337873, _a_(337872, _n_(337871, "plt", lambda: plt), "xlabel"), 'Games played')
_l_(337874)
_c_(337877, _a_(337876, _n_(337875, "plt", lambda: plt), "grid"))
_l_(337878)
_c_(337881, _a_(337880, _n_(337879, "plt", lambda: plt), "savefig"), 'English_10000.pdf', dpi='300')
_l_(337882)