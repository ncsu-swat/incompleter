# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46057819/attribute-error-method-object-has-no-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render
    _l_(413429)

except ImportError:
    pass
try:
    from django.http import Http404
    _l_(413431)

except ImportError:
    pass
try:
    from inventory.models import Item
    _l_(413433)

except ImportError:
    pass

def index(request):
    _l_(413447)

    items = _c_(413437, _a_(413436, _a_(413435, _n_(413434, "Item", lambda: Item), "objects"), "exclude"), aantal=0)
    _l_(413438)
    aux = _c_(413442, _n_(413439, "render", lambda: render), _n_(413440, "request", lambda: request), 'inventory/index.html', {
        'items': _n_(413441, "items", lambda: items),
    })
    _l_(413443)
    return aux
    aux = _c_(413445, _n_(413444, "HttpResponse", lambda: HttpResponse), '<p>In index view</p>')
    _l_(413446)
    return aux

def item_detail(request, id):
    _l_(413465)

    try:
        _l_(413459)

        item = _a_(413450, _a_(413449, _n_(413448, "Item", lambda: Item), "objects"), "get").id=_n_(413451, "id", lambda: (id)) #THIS ONE CAUSES PROBLEM???
        _l_(413452) #THIS ONE CAUSES PROBLEM???
    except _a_(413454, _n_(413453, "Item", lambda: Item), "DoesNotExist"):
        _l_(413458)

        raise _c_(413456, _n_(413455, "Http404", lambda: Http404), 'Dit item bestaat niet')
        _l_(413457)
    aux = _c_(413463, _n_(413460, "render", lambda: render), _n_(413461, "request", lambda: request), 'inventory/item_detail.html', {
        'item': _n_(413462, "item", lambda: item),
    })
    _l_(413464)
    return aux