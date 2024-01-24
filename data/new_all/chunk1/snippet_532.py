# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47012130/django-attributeerror-nonetype-object-has-no-attribute-method
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(402767, _n_(402765, "permission_classes", lambda: permission_classes), [_n_(402766, "UserPermission", lambda: UserPermission)])
class UserObject(_n_(402768, "GenericAPIView", lambda: GenericAPIView)):
    _l_(402899)


    def get_serializer_class(self):
        _l_(402777)


        if _a_(402771, _a_(402770, _n_(402769, "self", lambda: self), "request"), "method") == 'POST':
            _l_(402774)

            aux = _n_(402772, "ObjectPostSerializer", lambda: ObjectPostSerializer)
            _l_(402773)
            return aux
        aux = _n_(402775, "ObjectSerializer", lambda: ObjectSerializer)
        _l_(402776)
        return aux

    def post(self, request, user_id):
        _l_(402806)


        serializer = _c_(402781, _n_(402778, "ObjectSerializer", lambda: ObjectSerializer), data=_a_(402780, _n_(402779, "request", lambda: request), "data"))
        _l_(402782)
        if _c_(402785, _a_(402784, _n_(402783, "serializer", lambda: serializer), "is_valid")):
            _l_(402798)

            _c_(402789, _a_(402787, _n_(402786, "serializer", lambda: serializer), "save"), user_id=_n_(402788, "user_id", lambda: user_id))
            _l_(402790)
            aux = _c_(402796, _n_(402791, "Response", lambda: Response), _a_(402793, _n_(402792, "serializer", lambda: serializer), "data"), status=_a_(402795, _n_(402794, "status", lambda: status), "HTTP_201_CREATED"))
            _l_(402797)
            return aux
        aux = _c_(402804, _n_(402799, "Response", lambda: Response), _a_(402801, _n_(402800, "serializer", lambda: serializer), "errors"), status=_a_(402803, _n_(402802, "status", lambda: status), "HTTP_400_BAD_REQUEST"))
        _l_(402805)
        return aux

    def get(self, request, user_id):
        _l_(402831)


        try:
            _l_(402821)

            object = _c_(402811, _a_(402809, _a_(402808, _n_(402807, "Object", lambda: Object), "objects"), "filter"), user=_n_(402810, "user_id", lambda: user_id))
            _l_(402812)
        except _a_(402814, _n_(402813, "Object", lambda: Object), "DoesNotExist"):
            _l_(402820)

            aux = _c_(402818, _n_(402815, "Response", lambda: Response), status=_a_(402817, _n_(402816, "status", lambda: status), "HTTP_404_NOT_FOUND"))
            _l_(402819)
            return aux
        serializer = _c_(402824, _n_(402822, "ObjectSerializer", lambda: ObjectSerializer), _n_(402823, "object", lambda: object), many=True)
        _l_(402825)
        aux = _c_(402829, _n_(402826, "Response", lambda: Response), _a_(402828, _n_(402827, "serializer", lambda: serializer), "data"))
        _l_(402830)
        return aux

    def put(self, request, user_id):
        _l_(402873)


        try:
            _l_(402846)

            object = _c_(402836, _a_(402834, _a_(402833, _n_(402832, "Object", lambda: Object), "objects"), "get"), user=_n_(402835, "user_id", lambda: user_id))
            _l_(402837)
        except _a_(402839, _n_(402838, "Object", lambda: Object), "DoesNotExist"):
            _l_(402845)

            aux = _c_(402843, _n_(402840, "Response", lambda: Response), status=_a_(402842, _n_(402841, "status", lambda: status), "HTTP_404_NOT_FOUND"))
            _l_(402844)
            return aux
        serializer = _c_(402851, _n_(402847, "ObjectSerializer", lambda: ObjectSerializer), _n_(402848, "object", lambda: object), data=_a_(402850, _n_(402849, "request", lambda: request), "data"))
        _l_(402852)
        if _c_(402855, _a_(402854, _n_(402853, "serializer", lambda: serializer), "is_valid")):
            _l_(402865)

            _c_(402858, _a_(402857, _n_(402856, "serializer", lambda: serializer), "save"))
            _l_(402859)
            aux = _c_(402863, _n_(402860, "Response", lambda: Response), _a_(402862, _n_(402861, "serializer", lambda: serializer), "data"))
            _l_(402864)
            return aux
        aux = _c_(402871, _n_(402866, "Response", lambda: Response), _a_(402868, _n_(402867, "serializer", lambda: serializer), "errors"), status=_a_(402870, _n_(402869, "status", lambda: status), "HTTP_400_BAD_REQUEST"))
        _l_(402872)
        return aux

    def delete(self, request, user_id):
        _l_(402898)


        try:
            _l_(402888)

            object = _c_(402878, _a_(402876, _a_(402875, _n_(402874, "Object", lambda: Object), "objects"), "filter"), user=_n_(402877, "user_id", lambda: user_id))
            _l_(402879)
        except _a_(402881, _n_(402880, "Object", lambda: Object), "DoesNotExist"):
            _l_(402887)

            aux = _c_(402885, _n_(402882, "Response", lambda: Response), status=_a_(402884, _n_(402883, "status", lambda: status), "HTTP_404_NOT_FOUND"))
            _l_(402886)
            return aux
        _c_(402891, _a_(402890, _n_(402889, "object", lambda: object), "delete"))
        _l_(402892)
        aux = _c_(402896, _n_(402893, "Response", lambda: Response), status=_a_(402895, _n_(402894, "status", lambda: status), "HTTP_204_NO_CONTENT"))
        _l_(402897)
        return aux