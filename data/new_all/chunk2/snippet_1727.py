# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60274886/django-newbie-error-typeerror-view-must-be-a-callable-or-a-list-tuple-in-the
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render
    _l_(472237)

except ImportError:
    pass

# Create your views here.
def hello(request):
    _l_(472242)

    aux = _c_(472240, _n_(472238, "render", lambda: render), _n_(472239, "request", lambda: request),"myapp/templates/hello.html", {})
    _l_(472241)
    return aux