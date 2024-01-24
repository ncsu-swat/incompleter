# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62132107/typeerror-item-subject-is-no-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render
    _l_(656764)

except ImportError:
    pass
try:
    from shop.models import Category, Item, Comment
    _l_(656766)

except ImportError:
    pass
try:
    from django.http import HttpResponseRedirect, Http404, HttpResponse
    _l_(656768)

except ImportError:
    pass

def mainpage(request):
    _l_(656781)

    categorys = _c_(656774, _a_(656773, _c_(656772, _a_(656771, _a_(656770, _n_(656769, "Category", lambda: Category), "objects"), "all")), "order_by"), 'name')
    _l_(656775)
    aux = _c_(656779, _n_(656776, "render", lambda: render), _n_(656777, "request", lambda: request), 'shop/mainpage.html', {'categs':_n_(656778, "categorys", lambda: categorys)})
    _l_(656780)
    return aux

def items(request, categ_id):
    _l_(656798)

    try:
        _l_(656792)

        itemss = _c_(656786, _a_(656784, _a_(656783, _n_(656782, "Item", lambda: Item), "objects"), "get"), id = _n_(656785, "categ_id", lambda: categ_id))
        _l_(656787)
    except:
        _l_(656791)

        raise _c_(656789, _n_(656788, "Http404", lambda: Http404), "Not found")
        _l_(656790)
    aux = _c_(656796, _n_(656793, "render", lambda: render), _n_(656794, "request", lambda: request), 'shop/items.html', {'itemss':_n_(656795, "itemss", lambda: itemss)})
    _l_(656797)

    return aux

def info(request, item_id):
    _l_(656815)

    try:
        _l_(656809)

        item = _c_(656803, _a_(656801, _a_(656800, _n_(656799, "Item", lambda: Item), "objects"), "get"), id = _n_(656802, "item_id", lambda: item_id))
        _l_(656804)
    except:
        _l_(656808)

        raise _c_(656806, _n_(656805, "Http404", lambda: Http404), "No one item is no found")
        _l_(656807)
    aux = _c_(656813, _n_(656810, "render", lambda: render), _n_(656811, "request", lambda: request), 'shop/info.html', {"item":_n_(656812, "item", lambda: item)})
    _l_(656814)

    return aux