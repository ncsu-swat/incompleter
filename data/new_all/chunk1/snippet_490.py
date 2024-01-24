# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51466319/django2-attributeerror-in-urls-py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render
    _l_(400367)

except ImportError:
    pass

def home(request):
    _l_(400372)

    aux = _c_(400370, _n_(400368, "render", lambda: render), _n_(400369, "request", lambda: request), 'core/home.html')  
    _l_(400371)  
    return aux  