# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73841032/fastapi-router-type-error-untyped-decorator-males-function-untyped
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
router = _c_(443515, _n_(443514, "APIRouter", lambda: APIRouter))
_l_(443516)

@_c_(443519, _a_(443518, _n_(443517, "router", lambda: router), "post"), "/overview/{location_id}")
async def get_overview(location_id: _n_(443520, "str", lambda: str)) -> _n_(443521, "object", lambda: object):
    _l_(443529)

    if 4 not in _n_(443522, "fake_items_db", lambda: fake_items_db):
        _l_(443526)

        raise _c_(443524, _n_(443523, "HTTPException", lambda: HTTPException), status_code=404, detail="Item not found")
        _l_(443525)
    aux = _n_(443527, "overview", lambda: overview)
    _l_(443528)
    return aux