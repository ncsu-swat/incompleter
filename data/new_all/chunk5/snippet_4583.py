# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55058939/typeerror-create-got-multiple-values-for-keyword-argument-user
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from rest_framework import viewsets
    _l_(681896)

except ImportError:
    pass
try:
    from rest_framework.response import Response
    _l_(681898)

except ImportError:
    pass
try:
    from django_filters.rest_framework import DjangoFilterBackend
    _l_(681900)

except ImportError:
    pass
try:
    from rest_framework.decorators import action
    _l_(681902)

except ImportError:
    pass
try:
    from .models import Project, Module
    _l_(681904)

except ImportError:
    pass
try:
    from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet
    _l_(681906)

except ImportError:
    pass
try:
    from .serializers import ProjectSerializer, ModuleSerializer, TechnologySerializer, RequirementSerializer
    _l_(681908)

except ImportError:
    pass
try:
    from .models import *
    _l_(681910)

except ImportError:
    pass
try:
    from tags.models import Tag
    _l_(681912)

except ImportError:
    pass

# Create your views here.


class ProjectViewSet(_a_(681914, _n_(681913, "viewsets", lambda: viewsets), "ModelViewSet")):
    _l_(682037)

    """A viewset for viewing and manipulating user instances"""

    _c_(681916, _n_(681915, "print", lambda: print), "PROJECT VIEWSET")
    _l_(681917)
    serializer_class = _n_(681918, "ProjectSerializer", lambda: ProjectSerializer)
    _l_(681919)
    queryset = _c_(681923, _a_(681922, _a_(681921, _n_(681920, "Project", lambda: Project), "objects"), "all"))
    _l_(681924)
    lookup_field = 'slug'
    _l_(681925)
    filter_backends = (_n_(681926, "DjangoFilterBackend", lambda: DjangoFilterBackend), )
    _l_(681927)

    @_c_(681929, _n_(681928, "action", lambda: action), detail=True, methods=["GET"])
    def modules(self, request, id=None):
        _l_(681949)

        project = _c_(681932, _a_(681931, _n_(681930, "self", lambda: self), "get_object"))
        _l_(681933)
        modules = _c_(681938, _a_(681936, _a_(681935, _n_(681934, "Module", lambda: Module), "objects"), "filter"), project=_n_(681937, "project", lambda: project))
        _l_(681939)
        serializer = _c_(681942, _n_(681940, "ModuleSerializer", lambda: ModuleSerializer), _n_(681941, "modules", lambda: modules), many=True)
        _l_(681943)
        aux = _c_(681947, _n_(681944, "Response", lambda: Response), _a_(681946, _n_(681945, "serializer", lambda: serializer), "data"), status=200)
        _l_(681948)

        return aux

    @_c_(681951, _n_(681950, "action", lambda: action), detail=True, methods=["GET"])
    def technologies(self, request, id=None):
        _l_(681971)

        project = _c_(681954, _a_(681953, _n_(681952, "self", lambda: self), "get_object"))
        _l_(681955)
        technologies = _c_(681960, _a_(681958, _a_(681957, _n_(681956, "Technology", lambda: Technology), "objects"), "filter"), project=_n_(681959, "project", lambda: project))
        _l_(681961)
        serializer = _c_(681964, _n_(681962, "TechnologySerializer", lambda: TechnologySerializer), _n_(681963, "technologies", lambda: technologies), many=True)
        _l_(681965)
        aux = _c_(681969, _n_(681966, "Response", lambda: Response), _a_(681968, _n_(681967, "serializer", lambda: serializer), "data"), status=200)
        _l_(681970)

        return aux

    @_c_(681973, _n_(681972, "action", lambda: action), detail=True, methods=["GET"])
    def requirements(self, request, id=None):
        _l_(681993)

        project = _c_(681976, _a_(681975, _n_(681974, "self", lambda: self), "get_object"))
        _l_(681977)
        requirements = _c_(681982, _a_(681980, _a_(681979, _n_(681978, "Requirement", lambda: Requirement), "objects"), "filter"), project=_n_(681981, "project", lambda: project))
        _l_(681983)
        serializer = _c_(681986, _n_(681984, "RequirementSerializer", lambda: RequirementSerializer), _n_(681985, "requirements", lambda: requirements), many=True)
        _l_(681987)
        aux = _c_(681991, _n_(681988, "Response", lambda: Response), _a_(681990, _n_(681989, "serializer", lambda: serializer), "data"), status=200)
        _l_(681992)

        return aux

    @_c_(681995, _n_(681994, "action", lambda: action), detail=True, methods="POST")
    def project(self, request, id=None):
        _l_(682036)

        _c_(681997, _n_(681996, "print", lambda: print), 'POST')
        _l_(681998)
        user = _c_(682001, _a_(682000, _n_(681999, "self", lambda: self), "get_object"))
        _l_(682002)
        data = _a_(682004, _n_(682003, "request", lambda: request), "data")
        _l_(682005)
        _c_(682008, _n_(682006, "print", lambda: print), _n_(682007, "data", lambda: data))
        _l_(682009)
        _n_(682010, "data", lambda: data)["user"] = _a_(682012, _n_(682011, "user", lambda: user), "id")
        _l_(682013)
        serializer = _c_(682016, _n_(682014, "ProjectSerializer", lambda: ProjectSerializer), data=_n_(682015, "data", lambda: data))
        _l_(682017)
        if _c_(682020, _a_(682019, _n_(682018, "serializer", lambda: serializer), "is_valid")):
            _l_(682030)

            _c_(682023, _a_(682022, _n_(682021, "serializer", lambda: serializer), "save"))
            _l_(682024)
            aux = _c_(682028, _n_(682025, "Response", lambda: Response), _a_(682027, _n_(682026, "serializer", lambda: serializer), "data"), status=201)
            _l_(682029)
            return aux
        aux = _c_(682034, _n_(682031, "Response", lambda: Response), _a_(682033, _n_(682032, "serializer", lambda: serializer), "errors"), status=400)
        _l_(682035)
        return aux