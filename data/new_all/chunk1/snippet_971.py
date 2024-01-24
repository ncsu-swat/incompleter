# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61619201/typeerror-bulk-create-got-an-unexpected-keyword-argument-ignore-conflicts
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class GroupSerializer(_a_(392979, _n_(392978, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(393026)

    permissions = _c_(392980, PermissionSerializerGroup, many=True, required=False)
    _l_(392981)

    class Meta:
        _l_(392985)

        model = Group
        _l_(392982)
        fields = ('id', 'name', 'permissions')
        _l_(392983)
        extra_kwargs = {
            'name': {'validators': []},
        }
        _l_(392984)

    def create(self, validated_data):
        _l_(393025)

        _c_(392988, _n_(392986, "print", lambda: print), _n_(392987, "validated_data", lambda: validated_data))
        _l_(392989)
        permissions_data = _c_(392992, _a_(392991, _n_(392990, "validated_data", lambda: validated_data), "pop"), "permissions")
        _l_(392993)
        obj, group = _c_(392998, _a_(392996, _a_(392995, _n_(392994, "Group", lambda: Group), "objects"), "update_or_create"), name=_n_(392997, "validated_data", lambda: validated_data)["name"])
        _l_(392999)
        _c_(393003, _a_(393002, _a_(393001, _n_(393000, "obj", lambda: obj), "permissions"), "clear"))
        _l_(393004)
        for permission in _n_(393005, "permissions_data", lambda: permissions_data):
            _l_(393018)

            per = _c_(393010, _a_(393008, _a_(393007, _n_(393006, "Permission", lambda: Permission), "objects"), "get"), codename=_n_(393009, "permission", lambda: permission)["codename"])
            _l_(393011)
            _c_(393016, _a_(393014, _a_(393013, _n_(393012, "obj", lambda: obj), "permissions"), "add"), _n_(393015, "per", lambda: per))
            _l_(393017)
        _c_(393021, _a_(393020, _n_(393019, "obj", lambda: obj), "save"))
        _l_(393022)
        aux = _n_(393023, "obj", lambda: obj)
        _l_(393024)
        return aux