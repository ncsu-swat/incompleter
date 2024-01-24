# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74169850/mongodb-with-django-typeerror-model-instances-without-primary-key-value-are-un
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import uuid
    _l_(593542)

except ImportError:
    pass
try:
    from django.db import models
    _l_(593544)

except ImportError:
    pass


# Create your models here.
class ModernConnectUsers(_a_(593546, _n_(593545, "models", lambda: models), "Model")):
    _l_(593558)

    user_id = _c_(593552, _a_(593548, _n_(593547, "models", lambda: models), "UUIDField"), primary_key=True, default=_c_(593551, _a_(593550, _n_(593549, "uuid", lambda: uuid), "uuid4")))
    _l_(593553)
    user_name = _c_(593556, _a_(593555, _n_(593554, "models", lambda: models), "CharField"), max_length=30, null=False)
    _l_(593557)