# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55509211/how-to-resolve-object-of-type-attributeerror-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class InviteKeyCreateAllSerializer(_a_(475730, _n_(475729, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(475771)

    current_user = _c_(475732, _a_(475731, serializers, "SerializerMethodField"), '_user')
    _l_(475733)
    is_take = _c_(475735, _a_(475734, serializers, "SerializerMethodField"))
    _l_(475736)
    class Meta:
        _l_(475739)

        model = Invite_Key
        _l_(475737)
        exclude = [
            'user_submitter',
            'user_receiver',
            'uuid',
            'status',
            'is_taken',
            'is_locked',
            'claim_date',
            'expire_date',
        ]
        _l_(475738)

    # Use this method for the custom field
    def _user(self, obj):
        _l_(475750)

        request = _c_(475743, _n_(475740, "getattr", lambda: getattr), _a_(475742, _n_(475741, "self", lambda: self), "context"), 'request', None)
        _l_(475744)
        if _n_(475745, "request", lambda: request):
            _l_(475749)

            aux = _a_(475747, _n_(475746, "request", lambda: request), "user")
            _l_(475748)
            return aux

    def get_is_taken(self, obj):
        _l_(475752)

        aux = False
        _l_(475751)
        return aux

    def get_status(self, obj):
        _l_(475754)

        aux = 'valid'
        _l_(475753)
        return aux

    # end of custom fields

    def create(self, validated_data):
        _l_(475770)

        key = _c_(475757, _n_(475755, "Invite_Key", lambda: Invite_Key), user_submitter=_n_(475756, "validated_data", lambda: validated_data)['request.user'],
        )
        _l_(475758)
        _c_(475762, _a_(475760, _n_(475759, "key", lambda: key), "set_user_submitter"), _n_(475761, "validated_data", lambda: validated_data)['user_submitter'])
        _l_(475763)
        _c_(475766, _a_(475765, _n_(475764, "key", lambda: key), "save"))
        _l_(475767)
        aux = _n_(475768, "key", lambda: key)
        _l_(475769)
        return aux