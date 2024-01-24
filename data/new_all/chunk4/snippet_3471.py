# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73829248/unable-to-fetch-user-details-by-an-id-given-in-a-json-string-getting-a-type-er
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from urllib import response
    _l_(643194)

except ImportError:
    pass
try:
    from django.shortcuts import render
    _l_(643196)

except ImportError:
    pass
try:
    from django.http import JsonResponse
    _l_(643198)

except ImportError:
    pass
try:
    from rest_framework.response import Response
    _l_(643200)

except ImportError:
    pass
try:
    from rest_framework.decorators import api_view
    _l_(643202)

except ImportError:
    pass
try:
    from users.models import User, Team, Description
    _l_(643204)

except ImportError:
    pass
try:
    from .serializers import UserSerializer, TeamSerializer, DescriptionSerializer
    _l_(643206)

except ImportError:
    pass

# describe user
@_c_(643208, _n_(643207, "api_view", lambda: api_view), ["GET"])
def describe_user(request):
    _l_(643224)

    user = _c_(643214, _a_(643211, _a_(643210, _n_(643209, "User", lambda: User), "objects"), "get"), pk=_a_(643213, _n_(643212, "request", lambda: request), "data")["id"])
    _l_(643215)
    serializer = _c_(643218, _n_(643216, "UserSerializer", lambda: UserSerializer), _n_(643217, "user", lambda: user))
    _l_(643219)
    aux = _c_(643222, _n_(643220, "JsonResponse", lambda: JsonResponse), _n_(643221, "serializer", lambda: serializer), safe=False)
    _l_(643223)
    return aux