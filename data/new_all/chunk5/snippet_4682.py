# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53086733/attribute-error-in-python-setting-y-ticks-to-minutes
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from matplotlib.dates import MinuteLocator
    _l_(662504)

except ImportError:
    pass

fig, ax = _c_(662507, _a_(662506, _n_(662505, "plt", lambda: plt), "subplots"), figsize=(10, 6))
_l_(662508)
_c_(662514, _a_(662511, _a_(662510, _n_(662509, "ax", lambda: ax), "yaxis"), "set_major_formatter"), _c_(662513, _n_(662512, "MinuteLocator", lambda: MinuteLocator)))
_l_(662515)
_c_(662521, _a_(662517, _n_(662516, "ax", lambda: ax), "bar"), _a_(662519, _n_(662518, "df", lambda: df), "x"), _n_(662520, "df", lambda: df)['time_minutes'], width=25, align='center')
_l_(662522)