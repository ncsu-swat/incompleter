# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55509211/how-to-resolve-object-of-type-attributeerror-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class InviteKeyAllCreateView(_a_(463503, _n_(463502, "generics", lambda: generics), "CreateAPIView")):
    _l_(463571)

    """
    POST invitekey/
    """
    serializer_class = InviteKeyCreateAllSerializer
    _l_(463504)
    permission_classes = (IsAuthenticated,)
    _l_(463505)

    def post(self, request, *args, **kwargs):
        _l_(463570)

        user = _a_(463508, _a_(463507, _n_(463506, "self", lambda: self), "request"), "user")
        _l_(463509)
        try:
            _l_(463569)

            # get user count of keys
            cur_key_count = _c_(463519, _a_(463518, _c_(463517, _a_(463516, _c_(463515, _a_(463512, _a_(463511, _n_(463510, "Invite_Key", lambda: Invite_Key), "objects"), "filter"), user_submitter_id=_a_(463514, _n_(463513, "user", lambda: user), "id")), "order_by"), '-created_at'), "count"))
            _l_(463520)
            if _n_(463521, "cur_key_count", lambda: cur_key_count) > 0:
                _l_(463560)

                # now we get the latest one
                check_key = _c_(463527, _a_(463524, _a_(463523, _n_(463522, "Invite_Key", lambda: Invite_Key), "object"), "filter"), user_submitter_id=_a_(463526, _n_(463525, "user", lambda: user), "id"))[0]
                _l_(463528)
                now = _c_(463531, _a_(463530, _n_(463529, "datetime", lambda: datetime), "now"))
                _l_(463532)
                if _n_(463533, "now", lambda: now)-_c_(463535, _n_(463534, "timedelta", lambda: timedelta), days=3) <= _c_(463540, _a_(463538, _a_(463537, _n_(463536, "datetime", lambda: datetime), "datetime"), "strptime"), _n_(463539, "check_key", lambda: check_key)['created_at'], "%Y-%m-%dT%H:%M:%S.%fZ"):
                    _l_(463559)

                    serialized_data = _c_(463544, _n_(463541, "InviteKeyCreateAllSerializer", lambda: InviteKeyCreateAllSerializer), data=_a_(463543, _n_(463542, "request", lambda: request), "data"))
                    _l_(463545)
                    _c_(463548, _a_(463547, _n_(463546, "serialized_data", lambda: serialized_data), "is_valid"), raise_exception=True)
                    _l_(463549)
                    _c_(463552, _a_(463551, _n_(463550, "serialized_data", lambda: serialized_data), "save"))
                    _l_(463553)
                else:
                    aux = _c_(463557, _n_(463554, "Response", lambda: Response), data={
                            "message": "Sorry, you have recently created an Invite Key, try again some other time."
                        },
                        status=_a_(463556, _n_(463555, "status", lambda: status), "HTTP_400_BAD_REQUEST")
                    )
                    _l_(463558)
                    return aux
        except _n_(463561, "Exception", lambda: Exception) as e:
            _l_(463568)

            aux = _c_(463566, _n_(463562, "Response", lambda: Response), data={
                    "message": "The Invite Key could not be created.",
                    "error": _n_(463563, "e", lambda: e)
                },
                status=_a_(463565, _n_(463564, "status", lambda: status), "HTTP_400_BAD_REQUEST")
            )
            _l_(463567)
            return aux