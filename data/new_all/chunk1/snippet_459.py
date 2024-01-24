# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50539105/django-2-0-tutorial-attributeerror-at-polls-1-vote-reversemanytoonedescript
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.urls import path
    _l_(412410)

except ImportError:
    pass
try:
    from . import views
    _l_(412412)

except ImportError:
    pass

app_name = 'polls'
_l_(412413)
urlpatterns = [
    _c_(412419, _n_(412414, "path", lambda: path), '', _c_(412418, _a_(412417, _a_(412416, _n_(412415, "views", lambda: views), "IndexView"), "as_view")), name='index'),
    _c_(412425, _n_(412420, "path", lambda: path), '<int:pk>/', _c_(412424, _a_(412423, _a_(412422, _n_(412421, "views", lambda: views), "DetailView"), "as_view")), name='detail'),
    _c_(412431, _n_(412426, "path", lambda: path), '<int:pk>/results/', _c_(412430, _a_(412429, _a_(412428, _n_(412427, "views", lambda: views), "ResultsView"), "as_view")), name='results'),
    _c_(412435, _n_(412432, "path", lambda: path), '<int:question_id>/vote/', _a_(412434, _n_(412433, "views", lambda: views), "vote"), name='vote'),
]
_l_(412436)