# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(85032)

except ImportError:
    pass
try:
    from dateutil.parser import parse
    _l_(85034)

except ImportError:
    pass
date_series = _c_(85037, _a_(85036, _n_(85035, "pd", lambda: pd), "Series"), ['Jan 2015', 'Feb 2016', 'Mar 2017', 'Apr 2018', 'May 2019'])
_l_(85038)
_c_(85040, _n_(85039, "print", lambda: print), 'Original Series:')
_l_(85041)
_c_(85044, _n_(85042, "print", lambda: print), _n_(85043, "date_series", lambda: date_series))
_l_(85045)
_c_(85047, _n_(85046, "print", lambda: print), '\nNew dates:')
_l_(85048)
_c_(85051, _n_(85049, "print", lambda: print), _n_(85050, "result", lambda: result))
_l_(85052)