# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63318060/typeerror-formlistview-missing-1-required-positional-argument-request
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.urls import path
    _l_(421290)

except ImportError:
    pass
try:
    from .views      import FormListView
    _l_(421292)

except ImportError:
    pass

urlpatterns = [
    _c_(421296, _n_(421293, "path", lambda: path), '',            _c_(421295, _n_(421294, "FormListView", lambda: FormListView)),     name = 'home'),
    _c_(421300, _n_(421297, "path", lambda: path), 'success/',    _c_(421299, _n_(421298, "Success", lambda: Success)),          name = 'success')
]
_l_(421301)