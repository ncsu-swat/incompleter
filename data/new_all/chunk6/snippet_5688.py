# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62442246/django-attribute-error-str-object-homepage
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render
    _l_(350429)

except ImportError:
    pass
try:
    from django.views.generic import ListView
    _l_(350431)

except ImportError:
    pass
try:
    from .models import Post
    _l_(350433)

except ImportError:
    pass
# Create your views here.


class BlogListView(_n_(350434, "ListView", lambda: ListView)):
    _l_(350438)

    model = _n_(350435, "Post", lambda: Post)
    _l_(350436)
    template_name = 'home.html'
    _l_(350437)