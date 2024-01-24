# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56368432/typeerror-unhashable-type-collections-ordereddict
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class ProfileSerializer(_a_(420132, _n_(420131, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(420137)

    """Profile Serializer"""
    class Meta:
        _l_(420136)

        model = Profile
        _l_(420133)
        fields = ('user','profile_name','image','profile_title')
        _l_(420134)
        extra_kwargs = {
            'image': {'read_only': True},
            'profile_name': {'read_only': True},
            'profile_title': {'read_only': True},
        }
        _l_(420135)


class FriendsSerializer(_a_(420139, _n_(420138, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(420170)

    """Serializer For Team Mambers"""
    members = _c_(420141, _n_(420140, "ProfileSerializer", lambda: ProfileSerializer), many=True)
    _l_(420142)

    class Meta:
        _l_(420146)

        model = _n_(420143, "Friend", lambda: Friend)
        _l_(420144)
        fields = '__all__'
        _l_(420145)
    def create(self, validated_data):
        _l_(420169)

        _c_(420149, _n_(420147, "print", lambda: print), _n_(420148, "validated_data", lambda: validated_data))
        _l_(420150)
        user = _n_(420151, "validated_data", lambda: validated_data)['user']
        _l_(420152)
        members = _n_(420153, "validated_data", lambda: validated_data)['members']
        _l_(420154)

        instance = _c_(420159, _a_(420157, _a_(420156, _n_(420155, "Friend", lambda: Friend), "objects"), "create"), user=_n_(420158, "user", lambda: user))
        _l_(420160)
        _c_(420165, _a_(420163, _a_(420162, _n_(420161, "instance", lambda: instance), "members"), "add"), *_n_(420164, "members", lambda: members))
        _l_(420166)
        aux = _n_(420167, "instance", lambda: instance)
        _l_(420168)
        return aux



class FriendsViewSet(_n_(420171, "ModelViewSet", lambda: ModelViewSet)):
    _l_(420180)

    """ViewSet For TeamMembers Model"""

    serializer_class = _n_(420172, "FriendsSerializer", lambda: FriendsSerializer)
    _l_(420173)
    lookup_field = 'user'
    _l_(420174)
    queryset = _c_(420178, _a_(420177, _a_(420176, _n_(420175, "Friend", lambda: Friend), "objects"), "all"))
    _l_(420179)


class Friend(_a_(420182, _n_(420181, "models", lambda: models), "Model")):
    _l_(420197)

    user = _c_(420185, _a_(420183, models, "OneToOneField"), User, related_name='creator', on_delete=_a_(420184, models, "CASCADE"))
    _l_(420186)
    members = _c_(420188, _a_(420187, models, "ManyToManyField"), Profile, blank=True)
    _l_(420189)

    def __str__(self):
        _l_(420196)

        aux = _c_(420194, _n_(420190, "str", lambda: str), _a_(420193, _a_(420192, _n_(420191, "self", lambda: self), "user"), "username"))
        _l_(420195)
        return aux