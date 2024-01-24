# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73829248/unable-to-fetch-user-details-by-an-id-given-in-a-json-string-getting-a-type-er
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from rest_framework import serializers
    _l_(627411)

except ImportError:
    pass
try:
    from users.models import Description, Team, User
    _l_(627413)

except ImportError:
    pass

class DescriptionSerializer(_a_(627415, _n_(627414, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(627420)

    class Meta:
        _l_(627419)

        model = _n_(627416, "Description", lambda: Description)
        _l_(627417)
        fields = "__all__"
        _l_(627418)

class TeamSerializer(_a_(627422, _n_(627421, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(627427)

    class Meta:
        _l_(627426)

        model = _n_(627423, "Team", lambda: Team)
        _l_(627424)
        fields = "__all__"
        _l_(627425)

class UserSerializer(_a_(627429, _n_(627428, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(627434)

    class Meta:
        _l_(627433)

        model = _n_(627430, "User", lambda: User)
        _l_(627431)
        fields = "__all__"
        _l_(627432)