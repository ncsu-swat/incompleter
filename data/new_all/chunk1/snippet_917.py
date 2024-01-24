# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/40511900/python-3-5-typeerror-a-bytes-like-object-is-required-not-str-using-truncate
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(398636, _a_(398635, _n_(398634, "app", lambda: app), "route"), "/")
def main():
    _l_(398649)

    pages = _c_(398643, _a_(398642, _c_(398641, _a_(398639, _a_(398638, _n_(398637, "db", lambda: db), "session"), "query"), _n_(398640, "Pages", lambda: Pages)), "all"))
    _l_(398644)
    aux = _c_(398647, _n_(398645, "render_template", lambda: render_template), 'index.html', title='Dashboard', pages=_n_(398646, "pages", lambda: pages))
    _l_(398648)
    return aux