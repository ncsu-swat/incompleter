# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58188060/attributeerror-module-calc-views-has-no-attribute-home
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render
    _l_(524044)

except ImportError:
    pass
try:
    from django.http import HttpResponse
    _l_(524046)

except ImportError:
    pass

def home(request):
    _l_(524050)

    aux = _c_(524048, _n_(524047, "HttpResponse", lambda: HttpResponse), "Hello World !")
    _l_(524049)
    return aux