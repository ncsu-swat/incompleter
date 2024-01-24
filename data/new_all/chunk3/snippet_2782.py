# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63129918/nameerror-name-jsonresponsemixin-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from programs.models import Program
    _l_(539771)

except ImportError:
    pass
try:
    from django.views.generic import ListView, DetailView
    _l_(539773)

except ImportError:
    pass
try:
    from django.http import JsonResponse
    _l_(539775)

except ImportError:
    pass
try:
    from django.views.generic.detail import SingleObjectTemplateResponseMixin
    _l_(539777)

except ImportError:
    pass
try:
    from django.views.generic.detail import BaseDetailView
    _l_(539779)

except ImportError:
    pass




class ProgramListView(_n_(539780, "ListView", lambda: ListView), _n_(539781, "JSONResponseMixin", lambda: JSONResponseMixin), _n_(539782, "SingleObjectTemplateResponseMixin", lambda: SingleObjectTemplateResponseMixin)):
    _l_(539833)

    
    model = _n_(539783, "Program", lambda: Program)
    _l_(539784)
    template_name = 'programs/program_list.html'
    _l_(539785)
    context_object_name = 'programs'
    _l_(539786)
    paginate_by = 6
    _l_(539787)
    paginate_orphans = 3
    _l_(539788)

    def get_queryset(self):
        _l_(539819)


        url_parameter = _c_(539793, _a_(539792, _a_(539791, _a_(539790, _n_(539789, "self", lambda: self), "request"), "GET"), "get"), 'q')
        _l_(539794)

        # if self.request.method == 'GET' and self.request.is_ajax():
        if _a_(539797, _a_(539796, _n_(539795, "self", lambda: self), "request"), "method") == 'GET':
            _l_(539806)

            queryset = _c_(539802, _a_(539800, _a_(539799, _n_(539798, "Program", lambda: Program), "objects"), "filter"), degree = _n_(539801, "url_parameter", lambda: url_parameter))
            _l_(539803)
            aux = _n_(539804, "queryset", lambda: queryset)
            _l_(539805)
            return aux

        if _a_(539809, _a_(539808, _n_(539807, "self", lambda: self), "request"), "method") == 'GET' and _n_(539810, "url_parameter", lambda: url_parameter) is None:
            _l_(539818)

            queryset = _c_(539814, _a_(539813, _a_(539812, _n_(539811, "Program", lambda: Program), "objects"), "all"))
            _l_(539815)
            aux = _n_(539816, "queryset", lambda: queryset)
            _l_(539817)
            return aux


    def render_to_response(self, context, url_parameter='BSc'):
        _l_(539832)

        # Look for a 'format=json' GET argument
        # if self.request.GET.get('format') == 'json':
        # if self.request.is_ajax():
        if _n_(539820, "url_parameter", lambda: url_parameter)=='BSc':
            _l_(539831)

            aux = _c_(539824, _a_(539822, _n_(539821, "self", lambda: self), "render_to_json_response"), _n_(539823, "context", lambda: context))
            _l_(539825)
            return aux
        else:
            aux = _c_(539829, _a_(539827, _n_(539826, "super", lambda: super)(), "render_to_response"), _n_(539828, "context", lambda: context))
            _l_(539830)
            return aux