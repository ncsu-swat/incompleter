# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66065071/got-attributeerror-when-attempting-to-get-a-value-for-field-text-on-serializer
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class CommentViewSet(_a_(572286, _n_(572285, "viewsets", lambda: viewsets), "ModelViewSet")):
    _l_(572307)

    serializer_class = CommentSerializer
    _l_(572287)
    permission_classes = [_a_(572288, permissions, "IsAuthenticatedOrReadOnly")]
    _l_(572289)
    def get_object(self, queryset = None, **kwargs):
        _l_(572300)

        item = _c_(572293, _a_(572292, _a_(572291, _n_(572290, "self", lambda: self), "kwargs"), "get"), 'pk')
        _l_(572294)
        aux = _c_(572298, _n_(572295, "get_list_or_404", lambda: get_list_or_404), _n_(572296, "Comment", lambda: Comment), post = _n_(572297, "item", lambda: item))
        _l_(572299)
        return aux

    def get_queryset(self):
        _l_(572306)

        aux = _c_(572304, _a_(572303, _a_(572302, _n_(572301, "Comment", lambda: Comment), "objects"), "all"))
        _l_(572305)
        return aux