# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43055952/typeerror-modelbase-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.conf.urls import url
    _l_(435795)

except ImportError:
    pass
try:
    from offense_api import views
    _l_(435797)

except ImportError:
    pass

urlpatterns = [
    _c_(435801, _n_(435798, "url", lambda: url), r'^seasons/$', _a_(435800, _n_(435799, "views", lambda: views), "season_list")),
    _c_(435805, _n_(435802, "url", lambda: url), r'^seasons/(?P<pk>[0-9]+)/$', _a_(435804, _n_(435803, "views", lambda: views), "season_detail")),
    _c_(435809, _n_(435806, "url", lambda: url), r'^characters/$', _a_(435808, _n_(435807, "views", lambda: views), "character_list")),
]
_l_(435810)