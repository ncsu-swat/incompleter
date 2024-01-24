# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68318786/pythondjangoattributeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.urls import path
    _l_(632394)

except ImportError:
    pass
try:
    from . import views
    _l_(632396)

except ImportError:
    pass

app_name = 'polls'
_l_(632397)

urlpatterns=[
    _c_(632401, _n_(632398, "path", lambda: path), "", _a_(632400, _n_(632399, "views", lambda: views), "index"), name="index"),
    _c_(632405, _n_(632402, "path", lambda: path), "<int:question_id>/", _a_(632404, _n_(632403, "views", lambda: views), "detail"), name="detail"),
    _c_(632411, _n_(632406, "path", lambda: path), "<int:pk>/results/", _c_(632410, _a_(632409, _a_(632408, _n_(632407, "views", lambda: views), "ResultsView"), "as_view")), name="results"),
    _c_(632415, _n_(632412, "path", lambda: path), "<int:question_id>/vote/", _a_(632414, _n_(632413, "views", lambda: views), "vote"), name="vote"),
]
_l_(632416)