# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67946350/attributeerror-when-trying-to-created-nested-serializer-in-django-rest-framework
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class CardSerializers(_a_(574888, _n_(574887, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(574892)

    class Meta:
        _l_(574891)

        model = Card
        _l_(574889)
        fields = ['id', 'number', 'name', 'set_id']
        _l_(574890)

class SetSerializers(_a_(574894, _n_(574893, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(574901)

    cards = _c_(574896, _n_(574895, "CardSerializers", lambda: CardSerializers))
    _l_(574897)

    class Meta:
        _l_(574900)

        model = Set
        _l_(574898)
        fields = ['id', 'code', 'name', 'releaseDate','cards']
        _l_(574899)