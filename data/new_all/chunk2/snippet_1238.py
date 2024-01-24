# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67819164/typeerror-at-ap1-checkbooks-type-object-is-not-iterable-return-auth-for
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from rest_framework import viewsets
    _l_(428115)

except ImportError:
    pass
try:
    from .serializers import  BookSerializer
    _l_(428117)

except ImportError:
    pass
try:
    from .models import Book
    _l_(428119)

except ImportError:
    pass
try:
    from rest_framework.authentication import TokenAuthentication
    _l_(428121)

except ImportError:
    pass
class BookViewSet(_a_(428123, _n_(428122, "viewsets", lambda: viewsets), "ModelViewSet")):
    _l_(428133)

    serializer_class = _n_(428124, "BookSerializer", lambda: BookSerializer)
    _l_(428125)
    queryset = _c_(428129, _a_(428128, _a_(428127, _n_(428126, "Book", lambda: Book), "objects"), "all"))
    _l_(428130)
    #Below line to give token authority
    authentication_classes = _n_(428131, "TokenAuthentication", lambda: (TokenAuthentication))
    _l_(428132)