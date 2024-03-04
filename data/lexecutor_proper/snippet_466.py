# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4186062/sqlalchemy-order-by-descending
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
session = _c_(63160, _n_(63159, "Session", lambda: Session))
_l_(63161)
auth_client_name = 'client3' 
_l_(63162) 
result_by_auth_client = _c_(63179, _a_(63178, _c_(63177, _a_(63172, _c_(63171, _a_(63167, _c_(63166, _a_(63164, _n_(63163, "session", lambda: session), "query"), _n_(63165, "ClientTotal", lambda: ClientTotal)), "filter"), _a_(63169, _n_(63168, "ClientTotal", lambda: ClientTotal), "client") ==
_n_(63170, "auth_client_name", lambda: auth_client_name)), "order_by"), _c_(63176, _a_(63175, _a_(63174, _n_(63173, "ClientTotal", lambda: ClientTotal), "id"), "desc"))), "all"))
_l_(63180)

for rbac in _n_(63181, "result_by_auth_client", lambda: result_by_auth_client):
    _l_(63187)

    _c_(63185, _n_(63182, "print", lambda: print), _a_(63184, _n_(63183, "rbac", lambda: rbac), "id")) 
    _l_(63186) 
_c_(63190, _a_(63189, _n_(63188, "session", lambda: session), "close"))
_l_(63191)

