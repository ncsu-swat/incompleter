# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49818728/typeerror-metaclass-conflict-python-3-django-2
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.views.generic.base import TemplateView
    _l_(386113)

except ImportError:
    pass
try:
    from generic.mixins import CategoryListMixin
    _l_(386115)

except ImportError:
    pass


class MainPageView(_n_(386116, "TemplateView", lambda: TemplateView), _n_(386117, "CategoryListMixin", lambda: CategoryListMixin)):
    _l_(386119)

    template_name = 'mainpage.html'
    _l_(386118)