# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62442246/django-attribute-error-str-object-homepage
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render
    _l_(345913)

except ImportError:
    pass
try:
    from django.views.generic import ListView
    _l_(345915)

except ImportError:
    pass
try:
    from .models import Post
    _l_(345917)

except ImportError:
    pass
# Create your views here.


class BlogListView(_n_(345918, "ListView", lambda: ListView)):
    _l_(345920)

    model = Posttemplate_name = 'home.html'
    _l_(345919)