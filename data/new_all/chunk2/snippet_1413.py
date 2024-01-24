# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63313991/attributeerror-function-object-has-no-attribute-as-view-whats-wrong
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.urls import path
    _l_(427469)

except ImportError:
    pass
try:
    from .views import FormListView
    _l_(427471)

except ImportError:
    pass

urlpatterns = [
    _c_(427476, _n_(427472, "path", lambda: path), '', _c_(427475, _a_(427474, _n_(427473, "FormListView", lambda: FormListView), "as_view")), name = 'home'),
    _c_(427481, _n_(427477, "path", lambda: path), 'success/', _c_(427480, _a_(427479, _n_(427478, "Success", lambda: Success), "as_view")), name = 'success')
]
_l_(427482)