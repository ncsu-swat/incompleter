# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75243740/attributeerror-tuple-object-has-no-attribute-sum
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(437322)

except ImportError:
    pass
try:
    import numpy
    _l_(437324)

except ImportError:
    pass

labels = 'Updated', 'Coverage (overall)', 'last 24 hours', 'Deleted', 'Deleted last 24 hours', 'Banned', 'Banned last 24 hours'
_l_(437325)
sizes = (6, 5.04, 0, 12, 0, 7, 7)
_l_(437326)
colors = ['yellowgreen', 'gold', 'lightskyblue', 'green', 'black', 'red', 'grey']
_l_(437327)

def absolute_value(val):
    _l_(437338)

    a  = _c_(437334, _a_(437329, _n_(437328, "numpy", lambda: numpy), "round"), _n_(437330, "val", lambda: val)/100.*_c_(437333, _a_(437332, _n_(437331, "sizes", lambda: sizes), "sum")), 0)
    _l_(437335)
    aux = _n_(437336, "a", lambda: a)
    _l_(437337)
    return aux

_c_(437345, _a_(437340, _n_(437339, "plt", lambda: plt), "pie"), _n_(437341, "sizes", lambda: sizes), labels=_n_(437342, "labels", lambda: labels), colors=_n_(437343, "colors", lambda: colors),
        autopct=_n_(437344, "absolute_value", lambda: absolute_value))
_l_(437346)

_c_(437349, _a_(437348, _n_(437347, "plt", lambda: plt), "axis"), 'equal')
_l_(437350)
_c_(437353, _a_(437352, _n_(437351, "plt", lambda: plt), "show"))
_l_(437354)