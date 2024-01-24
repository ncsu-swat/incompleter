# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49818728/typeerror-metaclass-conflict-python-3-django-2
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render
    _l_(404583)

except ImportError:
    pass
try:
    from django.views.generic.base import TemplateView
    _l_(404585)

except ImportError:
    pass
try:
    from django.views.generic.base import ContextMixin
    _l_(404587)

except ImportError:
    pass


class CategoryListMixin(_n_(404588, "ContextMixin", lambda: ContextMixin)):
    _l_(404602)

    def get_context_data(self, **kwargs):
        _l_(404601)

        context = _c_(404592, _a_(404590, _n_(404589, "super", lambda: super)(), "get_context_data"), **_n_(404591, "kwargs", lambda: kwargs))
        _l_(404593)
        _n_(404594, "context", lambda: context)['current_url'] = _a_(404597, _a_(404596, _n_(404595, "self", lambda: self), "request"), "path")
        _l_(404598)
        aux = _n_(404599, "context", lambda: context)
        _l_(404600)
        return aux

class MainPageView(_n_(404603, "TemplateView", lambda: TemplateView), _n_(404604, "CategoryListMixin", lambda: CategoryListMixin)):
    _l_(404606)

    template_name = 'mainpage.html'
    _l_(404605)