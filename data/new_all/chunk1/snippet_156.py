# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/38394598/typeerror-view-must-be-a-callable-or-a-list-tuple-in-the-case-of-include
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render
    _l_(378015)

except ImportError:
    pass
try:
    from django.http import HttpResponse
    _l_(378017)

except ImportError:
    pass
# Create your views here.
#function based views

def post_home(request):
    _l_(378023)

    response = "<h1>Success</h1>"
    _l_(378018)
    aux = _c_(378021, _n_(378019, "HttpResponse", lambda: HttpResponse), _n_(378020, "response", lambda: response))
    _l_(378022)
    return aux