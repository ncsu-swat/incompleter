# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48868516/type-error-with-django-post-method
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.conf.urls import url
    _l_(702572)

except ImportError:
    pass
try:
    from django.urls import path
    _l_(702574)

except ImportError:
    pass
try:
    from . import views
    _l_(702576)

except ImportError:
    pass


urlpatterns = [
    # match list,
    _c_(702580, _n_(702577, "url", lambda: url), r'^$', _a_(702579, _n_(702578, "views", lambda: views), "index"), name='index'),
    _c_(702584, _n_(702581, "url", lambda: url), r'^add/$', _a_(702583, _n_(702582, "views", lambda: views), "addTodo"), name='add'),

    # match id goes to detail view
    _c_(702590, _n_(702585, "url", lambda: url), r'^(?P<pk>[0-9]+)/$', _c_(702589, _a_(702588, _a_(702587, _n_(702586, "views", lambda: views), "DetailView"), "as_view")), name='detail'),
]
_l_(702591)