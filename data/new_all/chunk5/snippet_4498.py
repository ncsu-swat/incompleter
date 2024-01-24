# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56553165/how-to-fix-typeerror-catg-id-is-an-invalid-keyword-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from categories.models import Catg, Type, Product, Choice
    _l_(699351)

except ImportError:
    pass
try:
    from django.shortcuts import render
    _l_(699353)

except ImportError:
    pass

def ch(request, Type_id, Product_id, Catg_id):
    _l_(699387)

    ca = _c_(699358, _a_(699356, _a_(699355, _n_(699354, "Catg", lambda: Catg), "objects"), "get"), pk=_n_(699357, "Catg_id", lambda: Catg_id))
    _l_(699359)
    p = _c_(699364, _a_(699362, _a_(699361, _n_(699360, "Type", lambda: Type), "objects"), "get"), pk=_n_(699363, "Type_id", lambda: Type_id))
    _l_(699365)
    cho = _c_(699370, _a_(699368, _a_(699367, _n_(699366, "Product", lambda: Product), "objects"), "get"), pk=_n_(699369, "Product_id", lambda: Product_id))
    _l_(699371)
    alls = _c_(699375, _a_(699374, _a_(699373, _n_(699372, "Choice", lambda: Choice), "objects"), "all"))
    _l_(699376)
    context3 = {
        'p': _n_(699377, "p", lambda: p),
        'alls': _n_(699378, "alls", lambda: alls),
        'cho': _n_(699379, "cho", lambda: cho),
        'ca': _n_(699380, "ca", lambda: ca),
    }
    _l_(699381)
    aux = _c_(699385, _n_(699382, "render", lambda: render), _n_(699383, "request", lambda: request), "service providers.html", _n_(699384, "context3", lambda: context3))
    _l_(699386)
    return aux