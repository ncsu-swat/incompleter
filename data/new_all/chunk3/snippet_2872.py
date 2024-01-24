# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60381766/how-do-i-create-a-field-in-my-serializer-to-avoid-a-typeerror-cannot-unpack-no
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class AddressTypeField(_a_(540287, _n_(540286, "serializers", lambda: serializers), "PrimaryKeyRelatedField")):
    _l_(540321)


    queryset = _a_(540288, Address, "objects")
    _l_(540289)

    def to_internal_value(self, data):
        _l_(540320)

        if _c_(540292, _n_(540290, "type", lambda: type), _n_(540291, "data", lambda: data)) == _n_(540293, "dict", lambda: dict):
            _l_(540314)

            locality = _n_(540294, "data", lambda: data)['locality']
            _l_(540295)
            locality, created = _c_(540300, _a_(540298, _a_(540297, _n_(540296, "Locality", lambda: Locality), "objects"), "get_or_create"), **_n_(540299, "locality", lambda: locality))
            _l_(540301)
            _n_(540302, "data", lambda: data)['locality'] = _n_(540303, "locality", lambda: locality)
            _l_(540304)
            address, created = _c_(540309, _a_(540307, _a_(540306, _n_(540305, "Address", lambda: Address), "objects"), "create"), **_n_(540308, "data", lambda: data))
            _l_(540310)
            # Replace the dict with the ID of the newly obtained object
            data = _a_(540312, _n_(540311, "address", lambda: address), "pk")
            _l_(540313)
        aux = _c_(540318, _a_(540316, _n_(540315, "super", lambda: super)(), "to_internal_value"), _n_(540317, "data", lambda: data))
        _l_(540319)
        return aux
...
_l_(540322)

class CoopSerializer(_a_(540324, _n_(540323, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(540418)

    type = _c_(540325, CoopTypeField)
    _l_(540326)
    address = _c_(540328, _n_(540327, "AddressTypeField", lambda: AddressTypeField))
    _l_(540329)

    class Meta:
        _l_(540332)

        model = Coop
        _l_(540330)
        fields = ['id', 'name', 'type', 'address', 'enabled', 'phone', 'email', 'web_site']
        _l_(540331)

    def to_representation(self, instance):
        _l_(540354)

        rep = _c_(540336, _a_(540334, _n_(540333, "super", lambda: super)(), "to_representation"), _n_(540335, "instance", lambda: instance))
        _l_(540337)
        _n_(540338, "rep", lambda: rep)['type'] = _a_(540343, _c_(540342, _n_(540339, "CoopTypeSerializer", lambda: CoopTypeSerializer), _a_(540341, _n_(540340, "instance", lambda: instance), "type")), "data")
        _l_(540344)
        _n_(540345, "rep", lambda: rep)['address'] = _a_(540350, _c_(540349, _n_(540346, "AddressSerializer", lambda: AddressSerializer), _a_(540348, _n_(540347, "instance", lambda: instance), "address")), "data")
        _l_(540351)
        aux = _n_(540352, "rep", lambda: rep)
        _l_(540353)
        return aux

    def create(self, validated_data):
        _l_(540361)

        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        aux = _c_(540359, _a_(540357, _a_(540356, _n_(540355, "Coop", lambda: Coop), "objects"), "create"), **_n_(540358, "validated_data", lambda: validated_data))
        _l_(540360)
        return aux

    def update(self, instance, validated_data):
        _l_(540417)

        """
        Update and return an existing `Coop` instance, given the validated data.
        """
        _n_(540362, "instance", lambda: instance).name = _c_(540367, _a_(540364, _n_(540363, "validated_data", lambda: validated_data), "get"), 'name', _a_(540366, _n_(540365, "instance", lambda: instance), "name"))
        _l_(540368)
        _n_(540369, "instance", lambda: instance).type = _c_(540374, _a_(540371, _n_(540370, "validated_data", lambda: validated_data), "get"), 'type', _a_(540373, _n_(540372, "instance", lambda: instance), "type"))
        _l_(540375)
        _n_(540376, "instance", lambda: instance).address = _c_(540381, _a_(540378, _n_(540377, "validated_data", lambda: validated_data), "get"), 'address', _a_(540380, _n_(540379, "instance", lambda: instance), "address"))
        _l_(540382)
        _n_(540383, "instance", lambda: instance).enabled = _c_(540388, _a_(540385, _n_(540384, "validated_data", lambda: validated_data), "get"), 'enabled', _a_(540387, _n_(540386, "instance", lambda: instance), "enabled"))
        _l_(540389)
        _n_(540390, "instance", lambda: instance).phone = _c_(540395, _a_(540392, _n_(540391, "validated_data", lambda: validated_data), "get"), 'phone', _a_(540394, _n_(540393, "instance", lambda: instance), "phone"))
        _l_(540396)
        _n_(540397, "instance", lambda: instance).email = _c_(540402, _a_(540399, _n_(540398, "validated_data", lambda: validated_data), "get"), 'email', _a_(540401, _n_(540400, "instance", lambda: instance), "email"))
        _l_(540403)
        _n_(540404, "instance", lambda: instance).web_site = _c_(540409, _a_(540406, _n_(540405, "validated_data", lambda: validated_data), "get"), 'web_site', _a_(540408, _n_(540407, "instance", lambda: instance), "web_site"))
        _l_(540410)
        _c_(540413, _a_(540412, _n_(540411, "instance", lambda: instance), "save"))
        _l_(540414)
        aux = _n_(540415, "instance", lambda: instance)
        _l_(540416)
        return aux