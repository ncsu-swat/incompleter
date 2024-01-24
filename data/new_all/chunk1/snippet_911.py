# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42956867/attributeerror-function-object-has-no-attribute-views
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render
    _l_(386419)

except ImportError:
    pass
try:
    from blog.models import Blog, Category
    _l_(386421)

except ImportError:
    pass
try:
    from django.shortcuts import render_to_response, get_object_or_404
    _l_(386423)

except ImportError:
    pass


def index(request):
    _l_(386435)

    aux = _c_(386433, _n_(386424, "render_to_response", lambda: render_to_response), 'index.html', {
        'categories': _c_(386428, _a_(386427, _a_(386426, _n_(386425, "Category", lambda: Category), "objects"), "all")),
        'posts': _c_(386432, _a_(386431, _a_(386430, _n_(386429, "Blog", lambda: Blog), "objects"), "all"))[:5]
    })
    _l_(386434)
    return aux


def view_post(request, slug):
    _l_(386443)

    aux = _c_(386441, _n_(386436, "render_to_response", lambda: render_to_response), 'view_post.html', {
        'post': _c_(386440, _n_(386437, "get_object_or_404", lambda: get_object_or_404), _n_(386438, "Blog", lambda: Blog), slug=_n_(386439, "slug", lambda: slug))
    })
    _l_(386442)
    return aux


def view_category(request, slug):
    _l_(386458)

    category = _c_(386447, _n_(386444, "get_object_or_404", lambda: get_object_or_404), _n_(386445, "Category", lambda: Category), slug=_n_(386446, "slug", lambda: slug))
    _l_(386448)
    aux = _c_(386456, _n_(386449, "render_to_response", lambda: render_to_response), 'view_category.html', {
        'category': _n_(386450, "category", lambda: category),
        'posts': _c_(386455, _a_(386453, _a_(386452, _n_(386451, "Blog", lambda: Blog), "objects"), "filter"), category=_n_(386454, "category", lambda: category))[:5]
    })
    _l_(386457)
    return aux