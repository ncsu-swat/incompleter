# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56506781/how-to-fix-typeerror-if-no-direction-is-specified-key-or-list-must-be-an-inst
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(425654, _a_(425653, _n_(425652, "app", lambda: app), "route"), '/search')
def search():
    _l_(425713)

    """Route for full text search bar"""
    page_limit = 6 #Logic for pagination
    _l_(425655) #Logic for pagination
    current_page = _c_(425661, _n_(425656, "int", lambda: int), _c_(425660, _a_(425659, _a_(425658, _n_(425657, "request", lambda: request), "args"), "get"), 'current_page', 1))
    _l_(425662)
    db_query = _a_(425664, _n_(425663, "request", lambda: request), "args")['db_query']
    _l_(425665)
    total = _c_(425671, _a_(425669, _a_(425668, _a_(425667, _n_(425666, "mongo", lambda: mongo), "db"), "recipe"), "create_index"), {'$text': {'$search': _n_(425670, "db_query", lambda: db_query) }})
    _l_(425672)
    t_total = _c_(425676, _n_(425673, "len", lambda: len), [_n_(425674, "x", lambda: x) for x in _n_(425675, "total", lambda: total)])
    _l_(425677)
    pages = _c_(425686, _n_(425678, "range", lambda: range), 1, _c_(425685, _n_(425679, "int", lambda: int), _c_(425684, _a_(425681, _n_(425680, "math", lambda: math), "ceil"), _n_(425682, "t_total", lambda: t_total) / _n_(425683, "page_limit", lambda: page_limit))) + 1)
    _l_(425687)
    results = _c_(425704, _a_(425702, _c_(425701, _a_(425698, _c_(425697, _a_(425694, _c_(425693, _a_(425691, _a_(425690, _a_(425689, _n_(425688, "mongo", lambda: mongo), "db"), "recipe"), "find"), {'$text': {'$search': _n_(425692, "db_query", lambda: db_query) }}), "sort"), '_id', _a_(425696, _n_(425695, "pymongo", lambda: pymongo), "ASCENDING")), "skip"), (_n_(425699, "current_page", lambda: current_page) - 1)*_n_(425700, "page_limit", lambda: page_limit)), "limit"), _n_(425703, "page_limit", lambda: page_limit))
    _l_(425705)
    aux = _c_(425711, _n_(425706, "render_template", lambda: render_template), 'search.html', results=_n_(425707, "results", lambda: results), pages=_n_(425708, "pages", lambda: pages), current_page=_n_(425709, "current_page", lambda: current_page), db_query=_n_(425710, "db_query", lambda: db_query))
    _l_(425712)
    return aux