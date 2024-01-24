# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61779471/i-kept-getting-typeerror-can-only-concatenate-str-not-nonetype-to-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(353636, _a_(353635, _n_(353634, "app", lambda: app), "route"), "/search", methods = ["GET", "POST"])
def search():
    _l_(353673)

    if "user_email" not in _n_(353637, "session", lambda: session):
        _l_(353641)

        aux = _c_(353639, _n_(353638, "render_template", lambda: render_template), "sign.html", error="Please Login First", work="Failed")
        _l_(353640)
        return aux

    if _a_(353643, _n_(353642, "request", lambda: request), "method") == 'GET':
        _l_(353672)

        title = _c_(353647, _a_(353646, _a_(353645, _n_(353644, "request", lambda: request), "form"), "get"), 'title')
        _l_(353648)
        isbn = _c_(353652, _a_(353651, _a_(353650, _n_(353649, "request", lambda: request), "form"), "get"), 'isbn')
        _l_(353653)
        author = _c_(353657, _a_(353656, _a_(353655, _n_(353654, "request", lambda: request), "form"), "get"), 'author')     
        _l_(353658)     
        searchs = _c_(353666, _a_(353665, _c_(353664, _a_(353660, _n_(353659, "db", lambda: db), "execute"), "SELECT * FROM books WHERE author iLIKE '%"+_n_(353661, "author", lambda: author)+"%' OR title iLIKE '%"+_n_(353662, "title", lambda: title)+"%' OR isbn iLIKE '%"+_n_(353663, "isbn", lambda: isbn)+"%'"), "fetchall"))
        _l_(353667)
        aux = _c_(353670, _n_(353668, "render_template", lambda: render_template), 'search.html', work = 'Success', searchs = _n_(353669, "searchs", lambda: searchs) )
        _l_(353671)
        return aux