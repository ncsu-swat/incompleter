# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/534839/how-to-create-a-guid-uuid-in-python

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import uuid
    _l_(1539863)

except ImportError:
    pass

def get_uuid_id():
    _l_(1539870)

    aux = _c_(1539868, _n_(1539864, "str", lambda: str), _c_(1539867, _a_(1539866, _n_(1539865, "uuid", lambda: uuid), "uuid4")))
    _l_(1539869)
    return aux

_c_(1539874, _n_(1539871, "print", lambda: print), _c_(1539873, _n_(1539872, "get_uuid_id", lambda: get_uuid_id))) 
_l_(1539875) 

