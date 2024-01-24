# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68263163/attributeerror-set-object-has-no-attribute-sa-instance-state-sqlalchemy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sqlalchemy.orm import relationship, declarative_base
    _l_(467880)

except ImportError:
    pass
try:
    from entities.utils import db
    _l_(467882)

except ImportError:
    pass
try:
    from entities.utils.utils import _repr
    _l_(467884)

except ImportError:
    pass
try:
    from sqlalchemy import Column, JSON, INTEGER, ForeignKey, Integer
    _l_(467886)

except ImportError:
    pass


class ResponseModel(_a_(467888, _n_(467887, "db", lambda: db), "Base")):
    _l_(467925)


    __tablename__ = 'responses'
    _l_(467889)

    id = _c_(467892, _n_(467890, "Column", lambda: Column), _n_(467891, "Integer", lambda: Integer), primary_key=True, autoincrement=True)
    _l_(467893)

    headers = _c_(467896, _n_(467894, "Column", lambda: Column), _n_(467895, "JSON", lambda: JSON), nullable=False)
    _l_(467897)
    status_code = _c_(467900, _n_(467898, "Column", lambda: Column), _n_(467899, "INTEGER", lambda: INTEGER), nullable=False)
    _l_(467901)
    body = _c_(467904, _n_(467902, "Column", lambda: Column), _n_(467903, "JSON", lambda: JSON), nullable=True)
    _l_(467905)


    def __init__(self, headers, status_code, body):
        _l_(467915)

        _n_(467906, "self", lambda: self).headers = _n_(467907, "headers", lambda: headers)
        _l_(467908)
        _n_(467909, "self", lambda: self).status_code = _n_(467910, "status_code", lambda: status_code)
        _l_(467911)
        _n_(467912, "self", lambda: self).body = _n_(467913, "body", lambda: body)
        _l_(467914)

    def __repr__(self):
        _l_(467924)

        aux = _c_(467922, _a_(467917, _n_(467916, "self", lambda: self), "_repr"), id=_a_(467919, _n_(467918, "self", lambda: self), "id"), status=_a_(467921, _n_(467920, "self", lambda: self), "status_code"))
        _l_(467923)
        return aux