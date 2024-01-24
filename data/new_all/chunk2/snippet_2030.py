# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68263163/attributeerror-set-object-has-no-attribute-sa-instance-state-sqlalchemy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sqlalchemy.orm import relationship
    _l_(432790)

except ImportError:
    pass
try:
    from entities.utils import db
    _l_(432792)

except ImportError:
    pass
try:
    from entities.utils.utils import _repr
    _l_(432794)

except ImportError:
    pass
try:
    from sqlalchemy import Column, String, JSON, INTEGER, ForeignKey, Integer, DateTime
    _l_(432796)

except ImportError:
    pass


class RequestModel(_a_(432798, _n_(432797, "db", lambda: db), "Base")):
    _l_(432852)

    __tablename__ = 'requests'
    _l_(432799)

    id = _c_(432802, _n_(432800, "Column", lambda: Column), _n_(432801, "Integer", lambda: Integer), primary_key=True,autoincrement=True)
    _l_(432803)
    headers = _c_(432806, _n_(432804, "Column", lambda: Column), _n_(432805, "JSON", lambda: JSON),nullable=False)
    _l_(432807)
    method = _c_(432810, _n_(432808, "Column", lambda: Column), _n_(432809, "String", lambda: String),nullable=False)
    _l_(432811)
    size = _c_(432814, _n_(432812, "Column", lambda: Column), _n_(432813, "INTEGER", lambda: INTEGER),nullable=False)
    _l_(432815)
    timestamp_end = _c_(432818, _n_(432816, "Column", lambda: Column), _n_(432817, "DateTime", lambda: DateTime),nullable=False)
    _l_(432819)
    timestamp_start = _c_(432822, _n_(432820, "Column", lambda: Column), _n_(432821, "DateTime", lambda: DateTime),nullable=False)
    _l_(432823)
    status_code = _c_(432826, _n_(432824, "Column", lambda: Column), _n_(432825, "INTEGER", lambda: INTEGER),nullable=False)
    _l_(432827)
    body = _c_(432830, _n_(432828, "Column", lambda: Column), _n_(432829, "JSON", lambda: JSON),nullable=True)
    _l_(432831)
    url = _c_(432834, _n_(432832, "Column", lambda: Column), _n_(432833, "String", lambda: String),nullable=False)
    _l_(432835)



    response_id =  _c_(432840, _n_(432836, "Column", lambda: Column), _n_(432837, "INTEGER", lambda: INTEGER),_c_(432839, _n_(432838, "ForeignKey", lambda: ForeignKey), 'responses.id'))
    _l_(432841)


    def __init__(self,method,status_code,url):
        _l_(432851)

        _n_(432842, "self", lambda: self).method = _n_(432843, "method", lambda: method)
        _l_(432844)
        _n_(432845, "self", lambda: self).status_code = _n_(432846, "status_code", lambda: status_code)
        _l_(432847)
        _n_(432848, "self", lambda: self).url = _n_(432849, "url", lambda: url)
        _l_(432850)