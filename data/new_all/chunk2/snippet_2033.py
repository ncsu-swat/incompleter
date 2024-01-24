# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68263163/attributeerror-set-object-has-no-attribute-sa-instance-state-sqlalchemy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(464293)

except ImportError:
    pass
try:
    from sqlalchemy import create_engine
    _l_(464295)

except ImportError:
    pass
try:
    from sqlalchemy.orm import Session
    _l_(464297)

except ImportError:
    pass
try:
    from sqlalchemy.ext.declarative import declarative_base
    _l_(464299)

except ImportError:
    pass
try:
    import datetime
    _l_(464301)

except ImportError:
    pass
try:
    from entities.models.Request import RequestModel
    _l_(464303)

except ImportError:
    pass
try:
    from entities.models.Response import ResponseModel
    _l_(464305)

except ImportError:
    pass
try:
    from entities.models.Session import SessionModel
    _l_(464307)

except ImportError:
    pass





engine = _c_(464309, _n_(464308, "create_engine", lambda: create_engine), 'postgresql://XXX:XXX@localhost:5423/XXXX')
_l_(464310)
Base = _c_(464312, _n_(464311, "declarative_base", lambda: declarative_base))
_l_(464313)
# create session and add objects
with _c_(464316, _n_(464314, "Session", lambda: Session), _n_(464315, "engine", lambda: engine)) as session:
    _l_(464381)

    response_object = _c_(464318, _n_(464317, "ResponseModel", lambda: ResponseModel), body={'22':'22'},status_code=402,headers={'test':'test'})
    _l_(464319)
    _c_(464323, _a_(464321, _n_(464320, "session", lambda: session), "add"), _n_(464322, "response_object", lambda: response_object))
    _l_(464324)
    _c_(464327, _a_(464326, _n_(464325, "session", lambda: session), "commit"))
    _l_(464328)

    object_1 = _c_(464330, _n_(464329, "RequestModel", lambda: RequestModel), 'POST', 402, 'www.intersecting.com/url?=parameter1&key')
    _l_(464331)
    _n_(464332, "object_1", lambda: object_1).headers = {'test':'19'}
    _l_(464333)
    _n_(464334, "object_1", lambda: object_1).body = {'test':'19'}
    _l_(464335)
    _n_(464336, "object_1", lambda: object_1).size = 512
    _l_(464337)
    _n_(464338, "object_1", lambda: object_1).timestamp_start = _c_(464342, _a_(464341, _a_(464340, _n_(464339, "datetime", lambda: datetime), "datetime"), "now"))
    _l_(464343)
    _n_(464344, "object_1", lambda: object_1).timestamp_end =_c_(464348, _a_(464347, _a_(464346, _n_(464345, "datetime", lambda: datetime), "datetime"), "now"))
    _l_(464349)
    object_2 = _n_(464350, "object_1", lambda: object_1)
    _l_(464351)
    _c_(464355, _a_(464353, _n_(464352, "session", lambda: session), "add"), _n_(464354, "object_1", lambda: object_1))
    _l_(464356)
    _c_(464359, _a_(464358, _n_(464357, "session", lambda: session), "commit"))
    _l_(464360)
    session_object = _c_(464362, _n_(464361, "SessionModel", lambda: SessionModel), 'www.test.com','test62','admin','3.12.13')
    _l_(464363)
    _c_(464366, _n_(464364, "print", lambda: print), _n_(464365, "session_object", lambda: session_object))
    _l_(464367)
    _n_(464368, "session_object", lambda: session_object).requests = {_n_(464369, "object_2", lambda: object_2),_n_(464370, "object_1", lambda: object_1)}
    _l_(464371)
    _c_(464375, _a_(464373, _n_(464372, "session", lambda: session), "add"), _n_(464374, "session_object", lambda: session_object))
    _l_(464376)
    _c_(464379, _a_(464378, _n_(464377, "session", lambda: session), "commit"))
    _l_(464380)