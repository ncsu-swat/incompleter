# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52421840/bar-plot-with-color-gradient-on-each-bar-error-typeerror-object-of-type-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(453036)

except ImportError:
    pass
quiz=[1,2,0,4,8,10]
_l_(453037)
_c_(453046, _a_(453039, _n_(453038, "plt", lambda: plt), "barh"), _c_(453044, _n_(453040, "range", lambda: range), _c_(453043, _n_(453041, "len", lambda: len), _n_(453042, "quiz", lambda: quiz))), _n_(453045, "quiz", lambda: quiz), align='center', alpha=0.5, color='blue')
_l_(453047)