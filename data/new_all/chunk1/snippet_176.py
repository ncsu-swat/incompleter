# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/34572553/django-attributeerror-nonetype-object-has-no-attribute-split
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(378730)

except ImportError:
    pass
try:
    from django.conf import settings
    _l_(378732)

except ImportError:
    pass
try:
    from django.http import Http404
    _l_(378734)

except ImportError:
    pass
try:
    from django.shortcuts import render
    _l_(378736)

except ImportError:
    pass
try:
    from django.template import Template
    _l_(378738)

except ImportError:
    pass
try:
    from django.utils._os import safe_join
    _l_(378740)

except ImportError:
    pass

# Create your views here.

def get_page_or_404(name):
    _l_(378774)

    """Returns page content as a Django template or raise 404 error"""
    try:
        _l_(378761)

        file_path = _c_(378745, _n_(378741, "safe_join", lambda: safe_join), _a_(378743, _n_(378742, "settings", lambda: settings), "STATIC_PAGES_DIRECTORY"), _n_(378744, "name", lambda: name))
        _l_(378746)
    except _n_(378747, "ValueError", lambda: ValueError):
        _l_(378751)

        raise _c_(378749, _n_(378748, "Http404", lambda: Http404), "Page Not Found")
        _l_(378750)
    else:
        if not _c_(378756, _a_(378754, _a_(378753, _n_(378752, "os", lambda: os), "path"), "exists"), _n_(378755, "file_path", lambda: file_path)):
            _l_(378760)

            raise _c_(378758, _n_(378757, "Http404", lambda: Http404), "Page Not Found")
            _l_(378759)

    with _c_(378764, _n_(378762, "open", lambda: open), _n_(378763, "file_path", lambda: file_path),"r", encoding='utf8') as f:
        _l_(378771)

        the_page = _c_(378769, _n_(378765, "Template", lambda: Template), _c_(378768, _a_(378767, _n_(378766, "f", lambda: f), "read")))
        _l_(378770)
    aux = _n_(378772, "the_page", lambda: the_page)
    _l_(378773)

    return aux

def page(request, slug='index'):
    _l_(378791)

    """ Render the requested page if found """
    file_name = _c_(378777, _a_(378775, '{0}.html', "format"), _n_(378776, "slug", lambda: slug))
    _l_(378778)
    page = _c_(378781, _n_(378779, "get_page_or_404", lambda: get_page_or_404), _n_(378780, "file_name", lambda: file_name))
    _l_(378782)
    context = {'slug': _n_(378783, "slug", lambda: slug), 'page': _n_(378784, "page", lambda: page)} 
    _l_(378785) 
    aux = _c_(378789, _n_(378786, "render", lambda: render), _n_(378787, "request", lambda: request), 'page.html', _n_(378788, "context", lambda: context))   # THE TRACEBACK POINTS AT THIS LINE, TOO
    _l_(378790)   # THE TRACEBACK POINTS AT THIS LINE, TOO
    return aux   # THE TRACEBACK POINTS AT THIS LINE, TOO