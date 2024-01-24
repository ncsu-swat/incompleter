# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55480813/how-to-fix-attributeerror-nonetype-object-has-no-attribute-id-and-self-asse
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.urls import path, re_path, include
    _l_(673946)

except ImportError:
    pass
try:
    from lists import views as list_views
    _l_(673948)

except ImportError:
    pass
try:
    from lists import urls as list_urls
    _l_(673950)

except ImportError:
    pass

urlpatterns = [
    #path('admin/', admin.site.urls),
    _c_(673954, _n_(673951, "re_path", lambda: re_path), '^$', _a_(673953, _n_(673952, "list_views", lambda: list_views), "home_page"), name="home"),
    _c_(673959, _n_(673955, "path", lambda: path), 'lists/', _c_(673958, _n_(673956, "include", lambda: include), _n_(673957, "list_urls", lambda: list_urls))),
    _c_(673963, _n_(673960, "re_path", lambda: re_path), '^lists/new/$', _a_(673962, _n_(673961, "list_views", lambda: list_views), "new_list"), name="new_list"),
    _c_(673967, _n_(673964, "re_path", lambda: re_path), '^lists/(\d+)/$', _a_(673966, _n_(673965, "list_views", lambda: list_views), "view_list"), name="view_list"),
    _c_(673971, _n_(673968, "re_path", lambda: re_path), '^lists/(\d+)/add_item$', _a_(673970, _n_(673969, "list_views", lambda: list_views), "add_item"), name="add_item"),
]
_l_(673972)