# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46050782/django-error-unsupported-operand-types-for-int-and-strtypeerror-at
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render
    _l_(406155)

except ImportError:
    pass
try:
    from django.http import HttpResponse
    _l_(406157)

except ImportError:
    pass


def index(request):
    _l_(406161)

    aux = _c_(406159, _n_(406158, "HttpResponse", lambda: HttpResponse), "<h1> Hi Cohen</h1>")
    _l_(406160)
    return aux