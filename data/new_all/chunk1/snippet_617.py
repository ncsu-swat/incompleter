# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56630585/how-can-i-solve-typeerror-at-post-new-in-django
# blog/urls.py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.urls import path
    _l_(393345)

except ImportError:
    pass
try:
    from . import views
    _l_(393347)

except ImportError:
    pass
urlpatterns = [
    _c_(393353, _n_(393348, "path", lambda: path), 'post/new/', _c_(393352, _a_(393351, _a_(393350, _n_(393349, "views", lambda: views), "BlogCreateView"), "as_view")), name='post_new'),
]
_l_(393354)