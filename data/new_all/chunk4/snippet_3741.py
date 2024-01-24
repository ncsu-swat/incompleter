# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68905652/turbogears2-typeerror-redirect-got-an-unexpected-keyword-argument-pagename
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(585133, _n_(585132, "expose", lambda: expose), 'wiki20.templates.page')
def _default(self, pagename="FrontPage"):
    _l_(585172)

    try:
        from sqlalchemy.exc import InvalidRequestError
        _l_(585135)

    except ImportError:
        pass

    try:
        _l_(585152)

        page = _c_(585144, _a_(585143, _c_(585142, _a_(585140, _c_(585139, _a_(585137, _n_(585136, "DBSession", lambda: DBSession), "query"), _n_(585138, "Page", lambda: Page)), "filter_by"), pagename=_n_(585141, "pagename", lambda: pagename)), "one"))
        _l_(585145)
    except _n_(585146, "InvalidRequestError", lambda: InvalidRequestError):
        _l_(585151)

        raise _c_(585149, _n_(585147, "redirect", lambda: redirect), "notfound", pagename=_n_(585148, "pagename", lambda: pagename))
        _l_(585150)

    content = _c_(585156, _n_(585153, "publish_parts", lambda: publish_parts), _a_(585155, _n_(585154, "page", lambda: page), "data"), writer_name="html")["html_body"]
    _l_(585157)
    root = _c_(585159, _n_(585158, "url", lambda: url), '/')
    _l_(585160)
    content = _c_(585165, _a_(585162, _n_(585161, "wikiwords", lambda: wikiwords), "sub"), r'<a href="%s\1">\1</a>' % _n_(585163, "root", lambda: root), _n_(585164, "content", lambda: content))
    _l_(585166)
    aux = _c_(585170, _n_(585167, "dict", lambda: dict), content=_n_(585168, "content", lambda: content), wikipage=_n_(585169, "page", lambda: page))
    _l_(585171)
    return aux