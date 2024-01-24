# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55480813/how-to-fix-attributeerror-nonetype-object-has-no-attribute-id-and-self-asse
#from django.contrib import admin
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.urls import path, re_path
    _l_(649893)

except ImportError:
    pass
try:
    from lists import views
    _l_(649895)

except ImportError:
    pass

urlpatterns = [
    #path('admin/', admin.site.urls),
    _c_(649899, _n_(649896, "re_path", lambda: re_path), '^new/$', _a_(649898, _n_(649897, "views", lambda: views), "new_list"), name="new_list"),
    _c_(649903, _n_(649900, "re_path", lambda: re_path), '^(\d+)/$', _a_(649902, _n_(649901, "views", lambda: views), "view_list"), name="view_list"),
    _c_(649907, _n_(649904, "re_path", lambda: re_path), '^(\d+)/add_item$', _a_(649906, _n_(649905, "views", lambda: views), "add_item"), name="add_item"),
]
_l_(649908)