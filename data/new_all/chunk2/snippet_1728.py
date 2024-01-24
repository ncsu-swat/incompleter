# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60274886/django-newbie-error-typeerror-view-must-be-a-callable-or-a-list-tuple-in-the
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.conf.urls import include, url
    _l_(450313)

except ImportError:
    pass

urlpatterns = ['', _c_(450315, _n_(450314, "url", lambda: url), 'hello/', 'views.hello', name='hello'),]
_l_(450316)