# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64882685/typeerror-object-of-type-user-is-not-json-serializable-why-is-this-happening
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class NewUserSerializer(_a_(428941, _n_(428940, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(428963)

    class Meta:
        _l_(428945)

        model = _a_(428942, models, "EndUser")
        _l_(428943)
        fields = ('id', 'first_name', 'last_name', 'email', 'title', 'user_type', 'packages', 'practice_area',
                  'office_phone', 'level', 'companies', 'country', 'password', 'firm', 'sectors', 'verticals', 'user_ptr')
        _l_(428944)

    def save(self, *args, **kwargs):
        _l_(428962)

        user = _c_(428950, _a_(428947, _n_(428946, "super", lambda: super)(), "save"), *_n_(428948, "args", lambda: args), **_n_(428949, "kwargs", lambda: kwargs))
        _l_(428951)
        _c_(428956, _a_(428953, _n_(428952, "user", lambda: user), "set_password"), _a_(428955, _n_(428954, "user", lambda: user), "password"))
        _l_(428957)
        _c_(428960, _a_(428959, _n_(428958, "user", lambda: user), "save"))
        _l_(428961)