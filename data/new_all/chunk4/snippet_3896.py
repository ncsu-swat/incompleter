# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65725015/typeerror-module-object-is-not-callable-django-3-render-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render
    _l_(645173)

except ImportError:
    pass
# from django.http import HttpResponse
# from django.template import RequestContext, loader
# from django.template import Context

def index(request):
    _l_(645181)

    """Placeholder index view"""
    _c_(645175, _n_(645174, "print", lambda: print), 'XXXX')
    _l_(645176)
    aux = _c_(645179, _n_(645177, "render", lambda: render), _n_(645178, "request", lambda: request), 'hello_world/index.html')
    _l_(645180)
    return aux

def test(request):
    _l_(645188)

    context = {'foo': 'bar'}
    _l_(645182)
    aux = _c_(645186, _n_(645183, "render", lambda: render), _n_(645184, "request", lambda: request), 'hello_world/index.html', _n_(645185, "context", lambda: context)) 
    _l_(645187) 
    return aux 