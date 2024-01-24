# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57689928/why-am-i-getting-this-error-attributeerror-str-object-has-no-attribute-deco
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.conf.urls import url
    _l_(399043)

except ImportError:
    pass
try:
    from . import views
    _l_(399045)

except ImportError:
    pass


urlpatterns = [
    _c_(399049, _n_(399046, "url", lambda: url), r'^$', _a_(399048, _n_(399047, "views", lambda: views), "register"), name='register_user'),
    _c_(399053, _n_(399050, "url", lambda: url), r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        _a_(399052, _n_(399051, "views", lambda: views), "activate_account"), name='activate'),
]
_l_(399054)