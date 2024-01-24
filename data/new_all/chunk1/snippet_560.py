# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60258163/nameerror-name-model-is-not-defined-after-importing-models-in-a-newly-created
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.utils import timezone
    _l_(385616)

except ImportError:
    pass
try:
    from django_smalluuid.models import SmallUUIDField, uuid_default
    _l_(385618)

except ImportError:
    pass
try:
    from django.db import models
    _l_(385620)

except ImportError:
    pass
try:
    import pytz
    _l_(385622)

except ImportError:
    pass
try:
    from .utilities import (calc_expiry_date,convert_date)
    _l_(385624)

except ImportError:
    pass
try:
    from monthdelta import monthdelta
    _l_(385626)

except ImportError:
    pass


class LiquorCostCentre(_a_(385628, _n_(385627, "models", lambda: models), "Model")):
    _l_(385637)

    cost_centre_id = _c_(385631, _a_(385630, _n_(385629, "models", lambda: models), "CharField"), max_length=250,null=True,blank=True,default="0304-05-05")
    _l_(385632)
    cost_centre_name = _c_(385635, _a_(385634, _n_(385633, "models", lambda: models), "CharField"), max_length=250,null=True,blank=True)
    _l_(385636)