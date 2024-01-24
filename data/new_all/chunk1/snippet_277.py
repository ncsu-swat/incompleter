# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67764955/init-takes-1-positional-argument-but-2-were-given-type-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib import admin
    _l_(413286)

except ImportError:
    pass
try:
    from .models import AvonleaClass
    _l_(413288)

except ImportError:
    pass

class AvonleaAdmin(_a_(413290, _n_(413289, "admin", lambda: admin), "ModelAdmin")):
    _l_(413292)

    readonly_fields = ('unitDateEntered',)
    _l_(413291)

_c_(413298, _a_(413295, _a_(413294, _n_(413293, "admin", lambda: admin), "site"), "register"), _n_(413296, "AvonleaClass", lambda: AvonleaClass), _n_(413297, "AvonleaAdmin", lambda: AvonleaAdmin))
_l_(413299)

class Birchleigh_ViewAdmin(_a_(413301, _n_(413300, "admin", lambda: admin), "ModelAdmin")):
    _l_(413303)

    readonly_fields = ('unitDateEntered',)
    _l_(413302)