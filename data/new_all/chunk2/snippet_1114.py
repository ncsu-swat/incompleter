# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60258163/nameerror-name-model-is-not-defined-after-importing-models-in-a-newly-created
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.utils import timezone
    _l_(438354)

except ImportError:
    pass
try:
    from django_smalluuid.models import SmallUUIDField, uuid_default
    _l_(438356)

except ImportError:
    pass
try:
    from django.db import models
    _l_(438358)

except ImportError:
    pass
try:
    import pytz
    _l_(438360)

except ImportError:
    pass
try:
    from .utilities import (calc_expiry_date,convert_date)
    _l_(438362)

except ImportError:
    pass
try:
    from monthdelta import monthdelta
    _l_(438364)

except ImportError:
    pass


class LiquorCostCentre(_a_(438366, _n_(438365, "models", lambda: models), "Model")):
    _l_(438375)

    cost_centre_id = _c_(438369, _a_(438368, _n_(438367, "models", lambda: models), "CharField"), max_length=250,null=True,blank=True,default="0304-05-05")
    _l_(438370)
    cost_centre_name = _c_(438373, _a_(438372, _n_(438371, "models", lambda: models), "CharField"), max_length=250,null=True,blank=True)
    _l_(438374)