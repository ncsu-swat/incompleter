# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2461702/why-is-ioc-di-not-common-in-python
# settings.py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': _n_(64808, "REDIS_URL", lambda: REDIS_URL) + '/1',
    },
    'local': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'snowflake',
    }
}
_l_(64809)

class FooView(_n_(64810, "APIView", lambda: APIView)):
    _l_(64823)

    # The "injected" dependencies:
    permission_classes = (IsAuthenticated, )
    _l_(64811)
    throttle_classes = (ScopedRateThrottle, )
    _l_(64812)
    parser_classes = (_a_(64813, parsers, "FormParser"), _a_(64814, parsers, "JSONParser"), _a_(64815, parsers, "MultiPartParser"))
    _l_(64816)
    renderer_classes = (_a_(64817, renderers, "JSONRenderer"),)
    _l_(64818)

    def get(self, request, *args, **kwargs):
        _l_(64820)

        pass
        _l_(64819)

    def post(self, request, *args, **kwargs):
        _l_(64822)

        pass
        _l_(64821)

