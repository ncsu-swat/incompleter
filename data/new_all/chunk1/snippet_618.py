# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56630585/how-can-i-solve-typeerror-at-post-new-in-django
# blog/views.py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.views.generic import ListView, DetailView
    _l_(378136)

except ImportError:
    pass
try:
    from django.views.generic.edit import CreateView
    _l_(378138)

except ImportError:
    pass
try:
    from . models import Post
    _l_(378140)

except ImportError:
    pass

class BlogCreateView(_n_(378141, "CreateView", lambda: CreateView)):
    _l_(378146)

    model = _n_(378142, "Post", lambda: Post)
    _l_(378143)
    template_name = 'post_new.html'
    _l_(378144)
    fields = '__all__'
    _l_(378145)