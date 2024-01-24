# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73590895/attributeerror-wsgirequest-object-has-no-attribute-get-i-got-this-error-ear
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.urls import path
    _l_(638975)

except ImportError:
    pass
try:
    from . import views
    _l_(638977)

except ImportError:
    pass

urlpatterns = [
    _c_(638981, _n_(638978, "path", lambda: path), '', _a_(638980, _n_(638979, "views", lambda: views), "projects")),
    _c_(638985, _n_(638982, "path", lambda: path), 'projects/<str:text>', _a_(638984, _n_(638983, "views", lambda: views), "dynamic"), name='project'),
    _c_(638989, _n_(638986, "path", lambda: path), 'create-project/', _a_(638988, _n_(638987, "views", lambda: views), "ProjectForm"), name='create-project')
]
_l_(638990)