# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61106188/i-am-getting-attributeerror-in-requestcontext-in-django
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render
    _l_(446043)

except ImportError:
    pass
try:
    from django.template import RequestContext
    _l_(446045)

except ImportError:
    pass

def survey(request):
    _l_(446052)

    aux = _c_(446050, _n_(446046, "render", lambda: render), _c_(446049, _n_(446047, "RequestContext", lambda: RequestContext), _n_(446048, "request", lambda: request)),'wfhApp/survey.html')
    _l_(446051)
    return aux