# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/38394598/typeerror-view-must-be-a-callable-or-a-list-tuple-in-the-case-of-include
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.conf.urls import url
    _l_(416481)

except ImportError:
    pass
try:
    from django.contrib import admin
    _l_(416483)

except ImportError:
    pass


urlpatterns = [
    _c_(416488, _n_(416484, "url", lambda: url), r'^admin/', _a_(416487, _a_(416486, _n_(416485, "admin", lambda: admin), "site"), "urls")),
    _c_(416490, _n_(416489, "url", lambda: url), r'^posts/$', "posts.views.post_home"), #posts is module and post_home 
]                                              # is a function in view. 
_l_(416491)                                              # is a function in view. 