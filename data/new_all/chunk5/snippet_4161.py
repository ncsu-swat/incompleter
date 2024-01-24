# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62132107/typeerror-item-subject-is-no-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render
    _l_(654819)

except ImportError:
    pass
try:
    from shop.models import Category, Item, Comment
    _l_(654821)

except ImportError:
    pass
try:
    from django.http import HttpResponseRedirect, Http404, HttpResponse
    _l_(654823)

except ImportError:
    pass

def mainpage(request):
    _l_(654836)

    categorys = _c_(654829, _a_(654828, _c_(654827, _a_(654826, _a_(654825, _n_(654824, "Category", lambda: Category), "objects"), "all")), "order_by"), 'name')
    _l_(654830)
    aux = _c_(654834, _n_(654831, "render", lambda: render), _n_(654832, "request", lambda: request), 'shop/mainpage.html', {'categs':_n_(654833, "categorys", lambda: categorys)})
    _l_(654835)
    return aux

def items(request, categ_id):
    _l_(654853)

    try:
        _l_(654847)

        itemss = _c_(654841, _a_(654839, _a_(654838, _n_(654837, "Item", lambda: Item), "objects"), "get"), id = _n_(654840, "categ_id", lambda: categ_id))
        _l_(654842)
    except:
        _l_(654846)

        raise _c_(654844, _n_(654843, "Http404", lambda: Http404), "Not found")
        _l_(654845)
    aux = _c_(654851, _n_(654848, "render", lambda: render), _n_(654849, "request", lambda: request), 'shop/items.html', {'itemss':_n_(654850, "itemss", lambda: itemss)})
    _l_(654852)

    return aux

def info(request, item_id):
    _l_(654870)

    try:
        _l_(654864)

        item = _c_(654858, _a_(654856, _a_(654855, _n_(654854, "Item", lambda: Item), "objects"), "get"), id = _n_(654857, "item_id", lambda: item_id))
        _l_(654859)
    except:
        _l_(654863)

        raise _c_(654861, _n_(654860, "Http404", lambda: Http404), "No one item is no found")
        _l_(654862)
    aux = _c_(654868, _n_(654865, "render", lambda: render), _n_(654866, "request", lambda: request), 'shop/info.html', {"item":_n_(654867, "item", lambda: item)})
    _l_(654869)

    return aux