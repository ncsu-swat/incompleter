# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62032946/drf-creating-new-objects-from-nested-representation-raises-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class BatchUserArticleList(_a_(558695, _n_(558694, "mixins", lambda: mixins), "ListModelMixin"),
                        _a_(558697, _n_(558696, "mixins", lambda: mixins), "CreateModelMixin"),
                        _a_(558699, _n_(558698, "generics", lambda: generics), "GenericAPIView")):
    _l_(558744)

    queryset = _c_(558702, _a_(558701, _a_(558700, UserArticle, "objects"), "all"))
    _l_(558703)
    serializer_class = BatchUserArticleSerializer
    _l_(558704)

    def create(self, request, *args, **kwargs):
        _l_(558735)

        serializer = _c_(558708, _n_(558705, "BatchUserArticleSerializer", lambda: BatchUserArticleSerializer), data=_a_(558707, _n_(558706, "request", lambda: request), "data"))
        _l_(558709)
        if not _c_(558712, _a_(558711, _n_(558710, "serializer", lambda: serializer), "is_valid")):
            _l_(558721)

            aux = _c_(558719, _a_(558714, _n_(558713, "response", lambda: response), "Response"), {'Message': 'POST failed',
                                  'Errors': _a_(558716, _n_(558715, "serializer", lambda: serializer), "errors")},
                                 _a_(558718, _n_(558717, "status", lambda: status), "HTTP_400_BAD_REQUEST"))
            _l_(558720)
            return aux
        _c_(558725, _a_(558723, _n_(558722, "self", lambda: self), "perform_create"), _n_(558724, "serializer", lambda: serializer))  # equal to serializer.save()
        _l_(558726)  # equal to serializer.save()
        aux = _c_(558733, _a_(558728, _n_(558727, "response", lambda: response), "Response"), _a_(558730, _n_(558729, "serializer", lambda: serializer), "data"), _a_(558732, _n_(558731, "status", lambda: status), "HTTP_201_CREATED"))
        _l_(558734)
        return aux

    def post(self, request, *args, **kwargs):
        _l_(558743)

        aux = _c_(558741, _a_(558737, _n_(558736, "self", lambda: self), "create"), _n_(558738, "request", lambda: request), *_n_(558739, "args", lambda: args), **_n_(558740, "kwargs", lambda: kwargs))
        _l_(558742)
        return aux