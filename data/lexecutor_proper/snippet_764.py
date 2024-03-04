# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6567831/how-to-perform-or-condition-in-django-queryset
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db.models import Q
    _l_(64757)

except ImportError:
    pass
_c_(64765, _a_(64760, _a_(64759, _n_(64758, "User", lambda: User), "objects"), "filter"), _c_(64762, _n_(64761, "Q", lambda: Q), income__gte=5000) | _c_(64764, _n_(64763, "Q", lambda: Q), income__isnull=True),category='income')
_l_(64766)

