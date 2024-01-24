# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59950609/typeerror-detail-missing-1-required-positional-argument-request
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.conf.urls import url, include
    _l_(390251)

except ImportError:
    pass
try:
    from rest_framework.urlpatterns import format_suffix_patterns
    _l_(390253)

except ImportError:
    pass
try:
    from .views import partial, Detailspartial, detail
    _l_(390255)

except ImportError:
    pass

urlpatterns = [
        _c_(390258, _n_(390256, "url", lambda: url), r'partial',_n_(390257, "partial", lambda: partial),name="partial"),
        _c_(390263, _n_(390259, "url", lambda: url), r'pardelete/(?P<pk>[0-9]+)/$', _c_(390262, _a_(390261, _n_(390260, "Detailspartial", lambda: Detailspartial), "as_view")), name="Partial details"),
        _c_(390266, _n_(390264, "url", lambda: url), r'detail',_n_(390265, "detail", lambda: detail),name="newfunction"),
]
_l_(390267)