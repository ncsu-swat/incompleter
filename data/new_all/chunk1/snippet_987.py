# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59066080/attributeerror-module-django-contrib-auth-has-no-attribute-models-what-am
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.conf.urls import url
    _l_(386596)

except ImportError:
    pass
try:
    from django.contrib.auth import views as auth_views
    _l_(386598)

except ImportError:
    pass
try:
    from django.urls import path
    _l_(386600)

except ImportError:
    pass
try:
    from . import views
    _l_(386602)

except ImportError:
    pass
app_name = 'login'
_l_(386603)

urlpatterns = [
    _c_(386607, _n_(386604, "path", lambda: path), 'ktupage/', _a_(386606, _n_(386605, "views", lambda: views), "ktupage"), name='ktupage'),
    _c_(386611, _n_(386608, "path", lambda: path), 'mgcourses/', _a_(386610, _n_(386609, "views", lambda: views), "mgcourses"), name='mgcourses'),
    _c_(386615, _n_(386612, "path", lambda: path), 'calicutcourses/', _a_(386614, _n_(386613, "views", lambda: views), "calicutcourses"), name='calicutcourses'),
    _c_(386619, _n_(386616, "path", lambda: path), 'mgcourses/mgaas/', _a_(386618, _n_(386617, "views", lambda: views), "mgaas"), name='mgaas'),
    _c_(386623, _n_(386620, "path", lambda: path), 'mgcourses/mgpara/', _a_(386622, _n_(386621, "views", lambda: views), "mgpara"), name='mgpara'),
    _c_(386627, _n_(386624, "path", lambda: path), 'calicutcourses/calicutaas/', _a_(386626, _n_(386625, "views", lambda: views), "calicutaas"), name='calicutaas'),
    _c_(386631, _n_(386628, "path", lambda: path), 'calicutcourses/calicutpara/', _a_(386630, _n_(386629, "views", lambda: views), "calicutpara"), name='calicutpara'),
    _c_(386637, _n_(386632, "path", lambda: path), 'login/', _c_(386636, _a_(386635, _a_(386634, _n_(386633, "auth_views", lambda: auth_views), "LoginView"), "as_view"), template_name='login.html'), name='login'),
    _c_(386643, _n_(386638, "path", lambda: path), 'logout/', _c_(386642, _a_(386641, _a_(386640, _n_(386639, "auth_views", lambda: auth_views), "LogoutView"), "as_view")),name='logout'),
    _c_(386649, _n_(386644, "path", lambda: path), 'signup/', _c_(386648, _a_(386647, _a_(386646, _n_(386645, "views", lambda: views), "signup"), "as_view")),name='signup'),
]
_l_(386650)