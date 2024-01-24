# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51348243/python-async-redis-gives-error-attributeerror-aexit
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sanic import Sanic
    _l_(706266)

except ImportError:
    pass
try:
    from sanic.response import json
    _l_(706268)

except ImportError:
    pass
try:
    import redis
    _l_(706270)

except ImportError:
    pass

app = _c_(706272, _n_(706271, "Sanic", lambda: Sanic))
_l_(706273)

# request.args['token']

@_c_(706276, _a_(706275, _n_(706274, "app", lambda: app), "route"), '/<id>')
async def test(request, id):
    _l_(706289)

    async with _c_(706279, _a_(706278, _n_(706277, "redis", lambda: redis), "StrictRedis"), host='0.0.0.0', port=6379, db=0) as r:
        _l_(706284)

        data = await _c_(706282, _a_(706281, _n_(706280, "r", lambda: r), "get"), "test")
        _l_(706283)
    aux = _c_(706287, _n_(706285, "json", lambda: json), {
        'data': _n_(706286, "data", lambda: data)
    })
    _l_(706288)

    return aux

if _n_(706290, "__name__", lambda: __name__) == '__main__':
    _l_(706295)

    _c_(706293, _a_(706292, _n_(706291, "app", lambda: app), "run"), host='0.0.0.0', port=9988)
    _l_(706294)