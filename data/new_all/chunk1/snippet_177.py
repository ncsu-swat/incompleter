# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/34572553/django-attributeerror-nonetype-object-has-no-attribute-split
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.conf.urls import include, url
    _l_(380759)

except ImportError:
    pass

urlpatterns = [
    _c_(380761, _n_(380760, "url", lambda: url), r'^page/(?P<slug>[-\w]+)/$', 'sitebuilder.views.page', name='page'),
    _c_(380763, _n_(380762, "url", lambda: url), r'^page$', 'sitebuilder.views.page', name='homepage'),
]
_l_(380764)