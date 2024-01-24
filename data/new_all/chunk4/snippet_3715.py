# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68812247/why-does-error-attribute-error-module-myapp-views-has-no-attribute-symbol-o
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render
    _l_(595017)

except ImportError:
    pass
try:
    from . import sub1
    _l_(595019)

except ImportError:
    pass
global symbol
_l_(595020)

def home(request):
    _l_(595025)

    aux = _c_(595023, _n_(595021, "render", lambda: render), _n_(595022, "request", lambda: request),"home.html")
    _l_(595024)
    return aux

def result(request):
    _l_(595045)

    global symbol
    _l_(595026)
    symbol = _a_(595028, _n_(595027, "request", lambda: request), "GET")['St']
    _l_(595029)
    pred_df= _c_(595032, _a_(595031, _n_(595030, "sub1", lambda: sub1), "my_main"))
    _l_(595033)
    ans=_c_(595038, _a_(595037, _c_(595036, _a_(595035, _n_(595034, "pred_df", lambda: pred_df), "tail")), "to_html"))
    _l_(595039)
    aux = _c_(595043, _n_(595040, "render", lambda: render), _n_(595041, "request", lambda: request),"result.html",{"ans":_n_(595042, "ans", lambda: ans)})
    _l_(595044)
    return aux