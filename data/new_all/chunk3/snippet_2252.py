# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55814099/flask-sqlalchemy-attributeerror-user-query-attribute-is-none
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
user = _c_(524020, _a_(524017, _n_(524016, "db_user", lambda: db_user), "find_user"), username=_n_(524018, "username", lambda: username), password=_n_(524019, "password", lambda: password))
_l_(524021)
# it raises: `AttributeError: 'NoneType' object has no attribute 'filter_by'`

user = _c_(524029, _a_(524028, _c_(524027, _a_(524024, _a_(524023, _n_(524022, "User", lambda: User), "query"), "filter_by"), username=_n_(524025, "username", lambda: username), password=_n_(524026, "password", lambda: password)), "all"))
_l_(524030)
# it raises: `AttributeError: 'NoneType' object has no attribute 'filter_by'`

user = _c_(524038, _a_(524037, _c_(524036, _a_(524033, _a_(524032, _n_(524031, "User", lambda: User), "query"), "filter"), username=_n_(524034, "username", lambda: username), password=_n_(524035, "password", lambda: password)), "all"))
_l_(524039)
# it raises: `AttributeError: 'NoneType' object has no attribute 'filter'`