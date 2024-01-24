# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55480813/how-to-fix-attributeerror-nonetype-object-has-no-attribute-id-and-self-asse
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import redirect, render
    _l_(659306)

except ImportError:
    pass
try:
    from lists.models import Item, List
    _l_(659308)

except ImportError:
    pass

def home_page(request):
    _l_(659331)

    if _a_(659310, _n_(659309, "request", lambda: request), "method") == 'POST':
        _l_(659321)

        _c_(659316, _a_(659313, _a_(659312, _n_(659311, "Item", lambda: Item), "objects"), "create"), text=_a_(659315, _n_(659314, "request", lambda: request), "POST")['item_text'])
        _l_(659317)
        aux = _c_(659319, _n_(659318, "redirect", lambda: redirect), '/')
        _l_(659320)
        return aux
    items = _c_(659325, _a_(659324, _a_(659323, _n_(659322, "Item", lambda: Item), "objects"), "all"))
    _l_(659326)
    aux = _c_(659329, _n_(659327, "render", lambda: render), _n_(659328, "request", lambda: request), 'home.html')
    _l_(659330)
    return aux

def view_list(request, list_id):
    _l_(659342)

    list_ = _c_(659335, _a_(659334, _a_(659333, _n_(659332, "List", lambda: List), "objects"), "get"))
    _l_(659336)
    aux = _c_(659340, _n_(659337, "render", lambda: render), _n_(659338, "request", lambda: request), 'list.html', {'list': _n_(659339, "list_", lambda: list_)})
    _l_(659341)
    return aux

def new_list(request):
    _l_(659361)

    list_ = _c_(659346, _a_(659345, _a_(659344, _n_(659343, "List", lambda: List), "objects"), "create"))
    _l_(659347)
    _c_(659354, _a_(659350, _a_(659349, _n_(659348, "Item", lambda: Item), "objects"), "create"), text=_a_(659352, _n_(659351, "request", lambda: request), "POST")['item_text'], list=_n_(659353, "list_", lambda: list_))
    _l_(659355)
    aux = _c_(659359, _n_(659356, "redirect", lambda: redirect), f'/lists/{_a_(659358, _n_(659357, "list", lambda: list), "id")}/')
    _l_(659360)
    return aux

def add_item(request, list_id):
    _l_(659381)

    list_ = _c_(659366, _a_(659364, _a_(659363, _n_(659362, 'List', lambda: List), 'objects'), 'get'), id=_n_(659365, 'list_id', lambda: list_id))
    _l_(659367)
    _c_(659374, _a_(659370, _a_(659369, _n_(659368, 'Item', lambda: Item), 'objects'), 'create'), text=_a_(659372, _n_(659371, 'request', lambda: request), 'POST')['item_text'], list=_n_(659373, 'list_', lambda: list_))
    _l_(659375)
    aux = _c_(659379, _n_(659376, 'redirect', lambda: redirect), f'/lists/{_a_(659378, _n_(659377, "list_", lambda: list_), "id")}/')
    _l_(659380)
    return aux