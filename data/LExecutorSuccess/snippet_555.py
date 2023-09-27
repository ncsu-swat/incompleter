# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2428092/creating-a-json-response-using-django-and-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.http import JsonResponse
    _l_(1543245)

except ImportError:
    pass

def your_view(request):
    _l_(1543251)

    json_object = {'key': "value"}
    _l_(1543246)
    aux = _c_(1543249, _n_(1543247, "JsonResponse", lambda: JsonResponse), _n_(1543248, "json_object", lambda: json_object))
    _l_(1543250)
    return aux

