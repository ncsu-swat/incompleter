# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56583458/matplotlib-is-now-giving-an-unknown-property-attributeerror-since-update-to-py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from astroplan import Observer, FixedTarget
    _l_(578450)

except ImportError:
    pass
try:
    import astropy.units as u
    _l_(578452)

except ImportError:
    pass
try:
    from astropy.time import Time
    _l_(578454)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(578456)

except ImportError:
    pass
try:
    from astroplan.plots import plot_sky
    _l_(578458)

except ImportError:
    pass
try:
    import numpy as np
    _l_(578460)

except ImportError:
    pass

time = _c_(578462, _n_(578461, "Time", lambda: Time), '2015-06-16 12:00:00')
_l_(578463)
subaru = _c_(578466, _a_(578465, _n_(578464, "Observer", lambda: Observer), "at_site"), 'subaru')
_l_(578467)
vega = _c_(578470, _a_(578469, _n_(578468, "FixedTarget", lambda: FixedTarget), "from_name"), 'Vega')
_l_(578471)
sunset_tonight = _c_(578475, _a_(578473, _n_(578472, "subaru", lambda: subaru), "sun_set_time"), _n_(578474, "time", lambda: time), which='nearest')
_l_(578476)
vega_rise = _c_(578481, _a_(578478, _n_(578477, "subaru", lambda: subaru), "target_rise_time"), _n_(578479, "time", lambda: time), _n_(578480, "vega", lambda: vega)) + 5*_a_(578483, _n_(578482, "u", lambda: u), "minute")
_l_(578484)
start = _c_(578489, _a_(578486, _n_(578485, "np", lambda: np), "max"), [_n_(578487, "sunset_tonight", lambda: sunset_tonight), _n_(578488, "vega_rise", lambda: vega_rise)])
_l_(578490)


_c_(578495, _n_(578491, "plot_sky", lambda: plot_sky), _n_(578492, "vega", lambda: vega), _n_(578493, "subaru", lambda: subaru), _n_(578494, "start", lambda: start))  
_l_(578496)  
_c_(578499, _a_(578498, _n_(578497, "plt", lambda: plt), "show"))  
_l_(578500)  