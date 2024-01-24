# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49309748/nameerror-name-django-filters-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render
    _l_(443158)

except ImportError:
    pass
try:
    from django_tables2 import RequestConfig
    _l_(443160)

except ImportError:
    pass
try:
    from django_tables2.export.export import TableExport
    _l_(443162)

except ImportError:
    pass
try:
    from django.contrib.postgres.search import SearchQuery, SearchRank
    _l_(443164)

except ImportError:
    pass
try:
    from django.template import RequestContext
    _l_(443166)

except ImportError:
    pass
try:
    from django.views.generic import *
    _l_(443168)

except ImportError:
    pass
try:
    from .models import *
    _l_(443170)

except ImportError:
    pass
try:
    from .tables import *
    _l_(443172)

except ImportError:
    pass
try:
    from .forms  import *
    _l_(443174)

except ImportError:
    pass
try:
    from .filters import Table1Filter
    _l_(443176)

except ImportError:
    pass

def table1(request):
    _l_(443191)

    filter = _c_(443184, _n_(443177, "Table1Filter", lambda: Table1Filter), _a_(443179, _n_(443178, "request", lambda: request), "GET"), queryset=_c_(443183, _a_(443182, _a_(443181, _n_(443180, "Table1", lambda: Table1), "objects"), "all")))
    _l_(443185)
    aux = _c_(443189, _n_(443186, "render", lambda: render), _n_(443187, "request", lambda: request), 'table1.html', {'filter': _n_(443188, "filter", lambda: filter)})
    _l_(443190)
    return aux