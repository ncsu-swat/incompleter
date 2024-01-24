# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52465552/builtins-typeerror-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(682361, _a_(682360, _n_(682359, "app", lambda: app), "route"), '/')
def getAllItems():
    _l_(682367)

    aux = _c_(682365, _n_(682362, "redirect", lambda: redirect), _c_(682364, _n_(682363, "url_for", lambda: url_for), 'getCategoryItems', category_name='ab', cat_id=1))
    _l_(682366)
    return aux


@_c_(682370, _a_(682369, _n_(682368, "app", lambda: app), "route"), '/<string:category_name>/items/')
def getCategoryItems(category_name, cat_id):
    _l_(682391)

    id = _n_(682371, "cat_id", lambda: cat_id);
    _l_(682372)
    items = _c_(682381, _a_(682380, _c_(682379, _a_(682377, _c_(682376, _a_(682374, _n_(682373, "session", lambda: session), "query"), _n_(682375, "Item", lambda: Item)), "filter_by"), category_id=_n_(682378, "id", lambda: id)), "all"))
    _l_(682382)
    output = ''
    _l_(682383)
    for item in _n_(682384, "items", lambda: items):
        _l_(682388)

        output += _a_(682386, _n_(682385, "item", lambda: item), "title") + '</br>'
        _l_(682387)
    aux = _n_(682389, "output", lambda: output)
    _l_(682390)
    return aux