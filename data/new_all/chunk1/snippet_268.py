# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57662873/filenotfounderror-winerror-3-the-system-cannot-find-the-path-specified
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from rest_framework import viewsets
    _l_(408991)

except ImportError:
    pass
try:
    from .models import Note
    _l_(408993)

except ImportError:
    pass
try:
    from .serializer import NoteSerializer
    _l_(408995)

except ImportError:
    pass

class NoteViewSet(_a_(408997, _n_(408996, "viewsets", lambda: viewsets), "ModelViewSet")):
    _l_(409005)

    queryset = _c_(409001, _a_(409000, _a_(408999, _n_(408998, "Note", lambda: Note), "objects"), "all"))
    _l_(409002)
    serializer_class = _n_(409003, "NoteSerializer", lambda: NoteSerializer)
    _l_(409004)