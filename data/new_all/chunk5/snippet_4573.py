# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55480813/how-to-fix-attributeerror-nonetype-object-has-no-attribute-id-and-self-asse
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.urls import path, re_path, include
    _l_(671677)

except ImportError:
    pass
try:
    from lists import views as list_views
    _l_(671679)

except ImportError:
    pass
try:
    from lists import urls as list_urls
    _l_(671681)

except ImportError:
    pass

urlpatterns = [
    #path('admin/', admin.site.urls),
    _c_(671685, _n_(671682, "re_path", lambda: re_path), '^$', _a_(671684, _n_(671683, "list_views", lambda: list_views), "home_page"), name="home"),
    _c_(671690, _n_(671686, "path", lambda: path), 'lists/', _c_(671689, _n_(671687, "include", lambda: include), _n_(671688, "list_urls", lambda: list_urls))),
    _c_(671694, _n_(671691, "re_path", lambda: re_path), '^lists/new/$', _a_(671693, _n_(671692, "list_views", lambda: list_views), "new_list"), name="new_list"),
    _c_(671698, _n_(671695, "re_path", lambda: re_path), '^lists/(\d+)/$', _a_(671697, _n_(671696, "list_views", lambda: list_views), "view_list"), name="view_list"),
    _c_(671702, _n_(671699, "re_path", lambda: re_path), '^lists/(\d+)/add_item$', _a_(671701, _n_(671700, "list_views", lambda: list_views), "add_item"), name="add_item"),
]
_l_(671703)