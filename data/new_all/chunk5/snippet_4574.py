# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55480813/how-to-fix-attributeerror-nonetype-object-has-no-attribute-id-and-self-asse
#from django.contrib import admin
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.urls import path, re_path
    _l_(685979)

except ImportError:
    pass
try:
    from lists import views
    _l_(685981)

except ImportError:
    pass

urlpatterns = [
    #path('admin/', admin.site.urls),
    _c_(685985, _n_(685982, "re_path", lambda: re_path), '^new/$', _a_(685984, _n_(685983, "views", lambda: views), "new_list"), name="new_list"),
    _c_(685989, _n_(685986, "re_path", lambda: re_path), '^(\d+)/$', _a_(685988, _n_(685987, "views", lambda: views), "view_list"), name="view_list"),
    _c_(685993, _n_(685990, "re_path", lambda: re_path), '^(\d+)/add_item$', _a_(685992, _n_(685991, "views", lambda: views), "add_item"), name="add_item"),
]
_l_(685994)