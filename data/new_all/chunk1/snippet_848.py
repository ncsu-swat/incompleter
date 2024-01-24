# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63101250/i-am-getting-an-attribute-error-while-trying-to-build-a-user-registration-form-u
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib import admin
    _l_(414782)

except ImportError:
    pass
try:
    from django.conf.urls import url
    _l_(414784)

except ImportError:
    pass
try:
    from django.urls import path, include
    _l_(414786)

except ImportError:
    pass
try:
    from . import views
    _l_(414788)

except ImportError:
    pass

app_name = 'basic_app'
_l_(414789)

urlpatterns = [
    _c_(414793, _n_(414790, "path", lambda: path), '', _a_(414792, _n_(414791, "views", lambda: views), "index"), name='index'),
    _c_(414797, _n_(414794, "path", lambda: path), 'register/', _a_(414796, _n_(414795, "views", lambda: views), "register"), name='register'),

]
_l_(414798)