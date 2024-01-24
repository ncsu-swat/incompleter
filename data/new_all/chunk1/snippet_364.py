# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67212594/attributeerror-pathdistribution-object-has-no-attribute-name
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from celery import Celery
    _l_(377021)

except ImportError:
    pass

app = _c_(377023, _n_(377022, "Celery", lambda: Celery))
_l_(377024)
_c_(377027, _a_(377026, _n_(377025, "app", lambda: app), "config_from_object"), 'celeryconfig')
_l_(377028)