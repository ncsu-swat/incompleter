# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54697609/why-am-i-getting-error-typeerror-string-indices-must-be-integers
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(473016)

except ImportError:
    pass
try:
    from pprint import pprint
    _l_(473018)

except ImportError:
    pass

with _c_(473020, _n_(473019, "open", lambda: open), 'driver.json', 'r') as f:
    _l_(473026)

    drivers_dict = _c_(473024, _a_(473022, _n_(473021, "json", lambda: json), "load"), _n_(473023, "f", lambda: f))
    _l_(473025)

for driver in _n_(473027, "drivers_dict", lambda: drivers_dict):
    _l_(473048)

    _c_(473030, _n_(473028, "print", lambda: print), _n_(473029, "driver", lambda: driver)['id'])
    _l_(473031)
    _c_(473034, _n_(473032, "print", lambda: print), _n_(473033, "driver", lambda: driver)['groupId'])
    _l_(473035)
    _c_(473038, _n_(473036, "print", lambda: print), _n_(473037, "driver", lambda: driver)['vehicleId'])
    _l_(473039)
    _c_(473042, _n_(473040, "print", lambda: print), _n_(473041, "driver", lambda: driver)['username'])
    _l_(473043)
    _c_(473046, _n_(473044, "print", lambda: print), _n_(473045, "driver", lambda: driver)['name'])
    _l_(473047)