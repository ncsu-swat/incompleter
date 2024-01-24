# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58030538/typeerror-str-object-is-not-callable-on-request-to-api
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from rest_framework.views import APIView
    _l_(537542)

except ImportError:
    pass
try:
    from rest_framework.response import Response
    _l_(537544)

except ImportError:
    pass
try:
    from . import models
    _l_(537546)

except ImportError:
    pass
try:
    from . import serializers
    _l_(537548)

except ImportError:
    pass


class ListBrand(_n_(537549, "APIView", lambda: APIView)):
    _l_(537569)

    def get(self, request, format=None):
        _l_(537568)

        brands = _c_(537554, _a_(537553, _a_(537552, _a_(537551, _n_(537550, "models", lambda: models), "Brand"), "objects"), "all"))
        _l_(537555)
        serializer = _c_(537559, _a_(537557, _n_(537556, "serializers", lambda: serializers), "BrandSerializer"), _n_(537558, "brands", lambda: brands), many=True)
        _l_(537560)
        data = _a_(537562, _n_(537561, "serializer", lambda: serializer), "data")
        _l_(537563)
        aux = _c_(537566, _n_(537564, "Response", lambda: Response), _n_(537565, "data", lambda: data))
        _l_(537567)
        return aux