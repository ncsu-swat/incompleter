# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68812247/why-does-error-attribute-error-module-myapp-views-has-no-attribute-symbol-o
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render
    _l_(642589)

except ImportError:
    pass
try:
    from . import sub1
    _l_(642591)

except ImportError:
    pass
global symbol
_l_(642592)

def home(request):
    _l_(642597)

    aux = _c_(642595, _n_(642593, "render", lambda: render), _n_(642594, "request", lambda: request),"home.html")
    _l_(642596)
    return aux

def result(request):
    _l_(642617)

    global symbol
    _l_(642598)
    symbol = _a_(642600, _n_(642599, "request", lambda: request), "GET")['St']
    _l_(642601)
    pred_df= _c_(642604, _a_(642603, _n_(642602, "sub1", lambda: sub1), "my_main"))
    _l_(642605)
    ans=_c_(642610, _a_(642609, _c_(642608, _a_(642607, _n_(642606, "pred_df", lambda: pred_df), "tail")), "to_html"))
    _l_(642611)
    aux = _c_(642615, _n_(642612, "render", lambda: render), _n_(642613, "request", lambda: request),"result.html",{"ans":_n_(642614, "ans", lambda: ans)})
    _l_(642616)
    return aux