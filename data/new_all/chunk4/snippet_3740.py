# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68905652/turbogears2-typeerror-redirect-got-an-unexpected-keyword-argument-pagename
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(589901, _n_(589900, "expose", lambda: expose), 'wiki20.templates.page')
def _default(self, pagename="FrontPage"):
    _l_(589940)

    try:
        from sqlalchemy.exc import InvalidRequestError
        _l_(589903)

    except ImportError:
        pass

    try:
        _l_(589920)

        page = _c_(589912, _a_(589911, _c_(589910, _a_(589908, _c_(589907, _a_(589905, _n_(589904, "DBSession", lambda: DBSession), "query"), _n_(589906, "Page", lambda: Page)), "filter_by"), pagename=_n_(589909, "pagename", lambda: pagename)), "one"))
        _l_(589913)
    except _n_(589914, "InvalidRequestError", lambda: InvalidRequestError):
        _l_(589919)

        raise _c_(589917, _n_(589915, "redirect", lambda: redirect), "notfound", pagename=_n_(589916, "pagename", lambda: pagename))
        _l_(589918)

    content = _c_(589924, _n_(589921, "publish_parts", lambda: publish_parts), _a_(589923, _n_(589922, "page", lambda: page), "data"), writer_name="html")["html_body"]
    _l_(589925)
    root = _c_(589927, _n_(589926, "url", lambda: url), '/')
    _l_(589928)
    content = _c_(589933, _a_(589930, _n_(589929, "wikiwords", lambda: wikiwords), "sub"), r'<a href="%s\1">\1</a>' % _n_(589931, "root", lambda: root), _n_(589932, "content", lambda: content))
    _l_(589934)
    aux = _c_(589938, _n_(589935, "dict", lambda: dict), content=_n_(589936, "content", lambda: content), wikipage=_n_(589937, "page", lambda: page))
    _l_(589939)
    return aux