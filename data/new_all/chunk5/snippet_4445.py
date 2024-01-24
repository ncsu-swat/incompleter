# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57628352/recieving-an-attribute-error-when-trying-to-add-a-new-view
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.http import HttpResponse
    _l_(680271)

except ImportError:
    pass
try:
    from django.shortcuts import render
    _l_(680273)

except ImportError:
    pass

# Create your views here.

def home(*args, **kwargs):
    _l_(680277)

    aux = _c_(680275, _n_(680274, "HttpResponse", lambda: HttpResponse), "<h1>Hello World!</h1>")
    _l_(680276)
    return aux