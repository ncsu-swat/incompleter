# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56148087/how-to-fix-typeerror-argument-of-type-function-is-not-iterable-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib import admin
    _l_(440978)

except ImportError:
    pass
try:
    from django.urls import path
    _l_(440980)

except ImportError:
    pass
try:
    from django.conf.urls import url
    _l_(440982)

except ImportError:
    pass
try:
    from demoapp.views import index,about,contact,clear
    _l_(440984)

except ImportError:
    pass
urlpatterns = [
    _c_(440989, _n_(440985, "path", lambda: path), 'admin/', _a_(440988, _a_(440987, _n_(440986, "admin", lambda: admin), "site"), "urls")),
    _c_(440993, _n_(440990, "url", lambda: url), r'^$' , _n_(440991, "index", lambda: index) , name=_n_(440992, "index", lambda: index)),
    _c_(440997, _n_(440994, "url", lambda: url), r'^about/$' , _n_(440995, "about", lambda: about) , name=_n_(440996, "about", lambda: about)),
    _c_(441001, _n_(440998, "url", lambda: url), r'^contact/$' , _n_(440999, "contact", lambda: contact) , name=_n_(441000, "contact", lambda: contact)),
    _c_(441005, _n_(441002, "url", lambda: url), r'^clear/$' , _n_(441003, "clear", lambda: clear) , name=_n_(441004, "clear", lambda: clear)),


]
_l_(441006)