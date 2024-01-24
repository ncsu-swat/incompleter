# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46050782/django-error-unsupported-operand-types-for-int-and-strtypeerror-at
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib import admin
    _l_(390647)

except ImportError:
    pass
try:
    from ofac_sdn.models import Ofac_Sdn
    _l_(390649)

except ImportError:
    pass
try:
    from ofac_sdn.models import Ofac_Add
    _l_(390651)

except ImportError:
    pass
try:
    from ofac_sdn.models import Ofac_Alt
    _l_(390653)

except ImportError:
    pass
# Register your models here.    
_c_(390658, _a_(390656, _a_(390655, _n_(390654, "admin", lambda: admin), "site"), "register"), _n_(390657, "Ofac_Sdn", lambda: Ofac_Sdn))    
_l_(390659)    
_c_(390664, _a_(390662, _a_(390661, _n_(390660, "admin", lambda: admin), "site"), "register"), _n_(390663, "Ofac_Add", lambda: Ofac_Add))
_l_(390665)
_c_(390670, _a_(390668, _a_(390667, _n_(390666, "admin", lambda: admin), "site"), "register"), _n_(390669, "Ofac_Alt", lambda: Ofac_Alt))
_l_(390671)