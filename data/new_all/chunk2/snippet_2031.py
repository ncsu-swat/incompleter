# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68263163/attributeerror-set-object-has-no-attribute-sa-instance-state-sqlalchemy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sqlalchemy.orm import relationship
    _l_(421056)

except ImportError:
    pass
try:
    from entities.utils import db
    _l_(421058)

except ImportError:
    pass
try:
    from entities.utils import utils
    _l_(421060)

except ImportError:
    pass
try:
    from sqlalchemy import Column, String, Integer, ForeignKey
    _l_(421062)

except ImportError:
    pass


class SessionModel(_a_(421064, _n_(421063, "db", lambda: db), "Base")):
    _l_(421123)

    __tablename__ = 'sessions'
    _l_(421065)

    id = _c_(421068, _n_(421066, "Column", lambda: Column), _n_(421067, "Integer", lambda: Integer), primary_key=True,autoincrement=True)
    _l_(421069)
    server = _c_(421072, _n_(421070, "Column", lambda: Column), _n_(421071, "String", lambda: String), nullable=False)
    _l_(421073)
    world = _c_(421076, _n_(421074, "Column", lambda: Column), _n_(421075, "String", lambda: String),nullable=False)
    _l_(421077)
    user = _c_(421080, _n_(421078, "Column", lambda: Column), _n_(421079, "String", lambda: String),nullable=False)
    _l_(421081)
    version = _c_(421084, _n_(421082, "Column", lambda: Column), _n_(421083, "String", lambda: String),nullable=False)
    _l_(421085)
    requests_id = _c_(421090, _n_(421086, "Column", lambda: Column), _n_(421087, "Integer", lambda: Integer), _c_(421089, _n_(421088, "ForeignKey", lambda: ForeignKey), 'requests.id'))
    _l_(421091)
    requests = _c_(421093, _n_(421092, "relationship", lambda: relationship), 'RequestModel')
    _l_(421094)



    def __init__(self,server,world,user,version):
        _l_(421107)

        _n_(421095, "self", lambda: self).server = _n_(421096, "server", lambda: server)
        _l_(421097)
        _n_(421098, "self", lambda: self).world = _n_(421099, "world", lambda: world)
        _l_(421100)
        _n_(421101, "self", lambda: self).user = _n_(421102, "user", lambda: user)
        _l_(421103)
        _n_(421104, "self", lambda: self).version = _n_(421105, "version", lambda: version)
        _l_(421106)



    def __repr__(self):
        _l_(421122)

        aux = _c_(421120, _a_(421109, _n_(421108, "self", lambda: self), "_repr"), id=_a_(421111, _n_(421110, "self", lambda: self), "id"),server=_a_(421113, _n_(421112, "self", lambda: self), "server"),
                          world=_a_(421115, _n_(421114, "self", lambda: self), "world"),user=_a_(421117, _n_(421116, "self", lambda: self), "user"),version=_a_(421119, _n_(421118, "self", lambda: self), "version"))
        _l_(421121)
        return aux