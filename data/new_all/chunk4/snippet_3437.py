# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74285492/pandas-causing-nonetype-error-in-matplotlib-plt-savefig-and-plt-show
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(582211)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(582213)

except ImportError:
    pass


df = _c_(582216, _a_(582215, _n_(582214, "pd", lambda: pd), "read_csv"), "data.csv")
_l_(582217)

time =  [0,10,20]
_l_(582218)
vel = [0,1,2]
_l_(582219)
fig,axes = _c_(582222, _a_(582221, _n_(582220, "plt", lambda: plt), "subplots"))
_l_(582223)
_c_(582228, _a_(582225, _n_(582224, "axes", lambda: axes), "plot"), _n_(582226, "time", lambda: time),_n_(582227, "vel", lambda: vel))
_l_(582229)
_c_(582232, _a_(582231, _n_(582230, "plt", lambda: plt), "show"))
_l_(582233)
_c_(582236, _a_(582235, _n_(582234, "plt", lambda: plt), "savefig"), fname = "pic.png" )
_l_(582237)