# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68685315/dynamic-serializer-django-rest-attributeerror-serializer-object-has-no-attr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class SNHUserSerializer(_a_(424947, _n_(424946, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(424979)

    class Meta:
        _l_(424950)

        model = SNHUser
        _l_(424948)
        fields = '__all__'
        _l_(424949)


    user = _c_(424951, UsersSerializer)
    _l_(424952)


    def create(self, validated_data):
        _l_(424970)

        # Create first the django user
        user_data = _c_(424955, _a_(424954, _n_(424953, "validated_data", lambda: validated_data), "pop"), 'user')
        _l_(424956)
        user = _c_(424961, _a_(424959, _a_(424958, _n_(424957, "User", lambda: User), "objects"), "create_user"), **_n_(424960, "user_data", lambda: user_data))
        _l_(424962)
        aux = _c_(424968, _a_(424965, _a_(424964, _n_(424963, "SNHUser", lambda: SNHUser), "objects"), "create"), user=_n_(424966, "user", lambda: user), **_n_(424967, "validated_data", lambda: validated_data))
        _l_(424969)
        # Create the layer of profile for the user
        return aux


    def to_representation(self, obj):
        _l_(424978)

        aux = _c_(424976, _a_(424974, _n_(424971, "super", lambda: super)(_n_(424972, "SNHUserSerializer", lambda: SNHUserSerializer), _n_(424973, "self", lambda: self)), "to_representation"), _n_(424975, "obj", lambda: obj))
        _l_(424977)
        return aux