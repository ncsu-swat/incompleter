# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55480813/how-to-fix-attributeerror-nonetype-object-has-no-attribute-id-and-self-asse
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import redirect, render
    _l_(667177)

except ImportError:
    pass
try:
    from lists.models import Item, List
    _l_(667179)

except ImportError:
    pass

def home_page(request):
    _l_(667202)

    if _a_(667181, _n_(667180, "request", lambda: request), "method") == 'POST':
        _l_(667192)

        _c_(667187, _a_(667184, _a_(667183, _n_(667182, "Item", lambda: Item), "objects"), "create"), text=_a_(667186, _n_(667185, "request", lambda: request), "POST")['item_text'])
        _l_(667188)
        aux = _c_(667190, _n_(667189, "redirect", lambda: redirect), '/')
        _l_(667191)
        return aux
    items = _c_(667196, _a_(667195, _a_(667194, _n_(667193, "Item", lambda: Item), "objects"), "all"))
    _l_(667197)
    aux = _c_(667200, _n_(667198, "render", lambda: render), _n_(667199, "request", lambda: request), 'home.html')
    _l_(667201)
    return aux

def view_list(request, list_id):
    _l_(667213)

    list_ = _c_(667206, _a_(667205, _a_(667204, _n_(667203, "List", lambda: List), "objects"), "get"))
    _l_(667207)
    aux = _c_(667211, _n_(667208, "render", lambda: render), _n_(667209, "request", lambda: request), 'list.html', {'list': _n_(667210, "list_", lambda: list_)})
    _l_(667212)
    return aux

def new_list(request):
    _l_(667232)

    list_ = _c_(667217, _a_(667216, _a_(667215, _n_(667214, "List", lambda: List), "objects"), "create"))
    _l_(667218)
    _c_(667225, _a_(667221, _a_(667220, _n_(667219, "Item", lambda: Item), "objects"), "create"), text=_a_(667223, _n_(667222, "request", lambda: request), "POST")['item_text'], list=_n_(667224, "list_", lambda: list_))
    _l_(667226)
    aux = _c_(667230, _n_(667227, "redirect", lambda: redirect), f'/lists/{_a_(667229, _n_(667228, "list", lambda: list), "id")}/')
    _l_(667231)
    return aux

def add_item(request, list_id):
    _l_(667252)

    list_ = _c_(667237, _a_(667235, _a_(667234, _n_(667233, 'List', lambda: List), 'objects'), 'get'), id=_n_(667236, 'list_id', lambda: list_id))
    _l_(667238)
    _c_(667245, _a_(667241, _a_(667240, _n_(667239, 'Item', lambda: Item), 'objects'), 'create'), text=_a_(667243, _n_(667242, 'request', lambda: request), 'POST')['item_text'], list=_n_(667244, 'list_', lambda: list_))
    _l_(667246)
    aux = _c_(667250, _n_(667247, 'redirect', lambda: redirect), f'/lists/{_a_(667249, _n_(667248, "list_", lambda: list_), "id")}/')
    _l_(667251)
    return aux