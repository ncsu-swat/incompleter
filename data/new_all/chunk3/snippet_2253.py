# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55814099/flask-sqlalchemy-attributeerror-user-query-attribute-is-none
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from catalog import app
    _l_(534154)

except ImportError:
    pass
try:
    from catalog.database import conn
    _l_(534156)

except ImportError:
    pass

...
_l_(534157)

_a_(534159, _n_(534158, "app", lambda: app), "config")['SQLALCHEMY_DATABASE_URI'] = _n_(534160, "conn", lambda: conn)
_l_(534161)
_a_(534163, _n_(534162, "app", lambda: app), "config")['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
_l_(534164)

# Create database connection
db_connection = _c_(534167, _n_(534165, "SQLAlchemy", lambda: SQLAlchemy), _n_(534166, "app", lambda: app))
_l_(534168)

# auto map tables
_n_(534169, "db_connection", lambda: db_connection).Model = _c_(534173, _n_(534170, "automap_base", lambda: automap_base), _a_(534172, _n_(534171, "db_connection", lambda: db_connection), "Model"))
_l_(534174)

# models
class User(_a_(534176, _n_(534175, "db_connection", lambda: db_connection), "Model"), _n_(534177, "UserMixin", lambda: UserMixin)):
    _l_(534182)

    __tablename__ = 'user'
    _l_(534178)

    roles = _c_(534180, relationship, 'Role', secondary='role_user',
                         backref=_c_(534179, backref, 'users', lazy='dynamic', cascade='all'), cascade="all, delete-orphan",
                         passive_deletes=True, single_parent=True)
    _l_(534181)


class Role(_a_(534184, _n_(534183, "db_connection", lambda: db_connection), "Model"), _n_(534185, "RoleMixin", lambda: RoleMixin)):
    _l_(534187)

    __tablename__ = 'role'
    _l_(534186)


class RoleUser(_a_(534189, _n_(534188, "db_connection", lambda: db_connection), "Model")):
    _l_(534191)

    __tablename__ = 'role_user'
    _l_(534190)

# datastore
db_user = _c_(534196, _n_(534192, "SQLAlchemyUserDatastore", lambda: SQLAlchemyUserDatastore), _n_(534193, "db_connection", lambda: db_connection), _n_(534194, "User", lambda: User), _n_(534195, "Role", lambda: Role))
_l_(534197)

security = _c_(534201, _n_(534198, "Security", lambda: Security), _n_(534199, "app", lambda: app), _n_(534200, "db_user", lambda: db_user))
_l_(534202)

...
_l_(534203)

# try to look for users by username and password

user = _c_(534208, _a_(534205, _n_(534204, "db_user", lambda: db_user), "find_user"), username=_n_(534206, "username", lambda: username), password=_n_(534207, "password", lambda: password))
_l_(534209)
# it raises: `AttributeError: 'NoneType' object has no attribute 'filter_by'`

user = _c_(534217, _a_(534216, _c_(534215, _a_(534212, _a_(534211, _n_(534210, "User", lambda: User), "query"), "filter_by"), username=_n_(534213, "username", lambda: username), password=_n_(534214, "password", lambda: password)), "all"))
_l_(534218)
# it raises: `AttributeError: 'NoneType' object has no attribute 'filter_by'`

user = _c_(534226, _a_(534225, _c_(534224, _a_(534221, _a_(534220, _n_(534219, "User", lambda: User), "query"), "filter"), username=_n_(534222, "username", lambda: username), password=_n_(534223, "password", lambda: password)), "all"))
_l_(534227)
# it raises: `AttributeError: 'NoneType' object has no attribute 'filter'`