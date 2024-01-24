# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61106188/i-am-getting-attributeerror-in-requestcontext-in-django
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.conf.urls import url
    _l_(443233)

except ImportError:
    pass
try:
    from wfhApp import views
    _l_(443235)

except ImportError:
    pass

app_name = 'wfhApp'
_l_(443236)

urlpatterns = [
     _c_(443240, _n_(443237, "url", lambda: url), r'^survey/$',_a_(443239, _n_(443238, "views", lambda: views), "survey"), name='survey'),
]
_l_(443241)