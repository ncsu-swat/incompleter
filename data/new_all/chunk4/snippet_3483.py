# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73590895/attributeerror-wsgirequest-object-has-no-attribute-get-i-got-this-error-ear
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render
    _l_(627223)

except ImportError:
    pass
try:
    from django.http import HttpResponse
    _l_(627225)

except ImportError:
    pass
try:
    from .models import Project
    _l_(627227)

except ImportError:
    pass
try:
    from .forms import ProjectForm
    _l_(627229)

except ImportError:
    pass


def projects(request):
    _l_(627242)

    objs = _c_(627233, _a_(627232, _a_(627231, _n_(627230, "Project", lambda: Project), "objects"), "all"))
    _l_(627234)
    context = {"projects": _n_(627235, "objs", lambda: objs)}
    _l_(627236)
    aux = _c_(627240, _n_(627237, "render", lambda: render), _n_(627238, "request", lambda: request), 'projects/project.html', _n_(627239, "context", lambda: context))
    _l_(627241)
    return aux


def dynamic(request, text):
    _l_(627254)

    obj = _c_(627247, _a_(627245, _a_(627244, _n_(627243, "Project", lambda: Project), "objects"), "get"), id=_n_(627246, "text", lambda: text))
    _l_(627248)
    aux = _c_(627252, _n_(627249, "render", lambda: render), _n_(627250, "request", lambda: request), 'projects/single-project.html', {'obj': _n_(627251, "obj", lambda: obj)})
    _l_(627253)
    return aux


def createproject(request):
    _l_(627265)

    form = _c_(627256, _n_(627255, "ProjectForm", lambda: ProjectForm))
    _l_(627257)
    context = {'form': _n_(627258, "form", lambda: form)}
    _l_(627259)
    aux = _c_(627263, _n_(627260, "render", lambda: render), _n_(627261, "request", lambda: request), 'projectform.html', _n_(627262, "context", lambda: context))
    _l_(627264)
    return aux