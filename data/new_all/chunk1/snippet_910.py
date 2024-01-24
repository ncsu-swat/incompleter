# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42956867/attributeerror-function-object-has-no-attribute-views
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.conf.urls import url
    _l_(395536)

except ImportError:
    pass
try:
    from django.contrib import admin
    _l_(395538)

except ImportError:
    pass
try:
    import WarblerTest
    _l_(395540)

except ImportError:
    pass


urlpatterns = {
    _c_(395545, _n_(395541, "url", lambda: url), r'^admin/', _a_(395544, _a_(395543, _n_(395542, "admin", lambda: admin), "site"), "urls")),
    (r'^$', _a_(395549, _a_(395548, _a_(395547, _n_(395546, "WarblerTest", lambda: WarblerTest), "blog"), "views"), "index")),
    _c_(395555, _n_(395550, "url", lambda: url), r'^blog/view/(?P<slug>[^\.]+).html',
        _a_(395554, _a_(395553, _a_(395552, _n_(395551, "WarblerTest", lambda: WarblerTest), "blog"), "views"), "view_post"),
        name='view_blog_post'),
    _c_(395561, _n_(395556, "url", lambda: url), r'^blog/category/(?P<slug>[^\.]+).html',
        _a_(395560, _a_(395559, _a_(395558, _n_(395557, "WarblerTest", lambda: WarblerTest), "blog"), "views"), "view_category"),
        name='view_blog_category'),
}
_l_(395562)