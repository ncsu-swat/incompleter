# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64236572/fastapi-typeerror-object-of-type-modelmetaclass-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sql.database import Base
    _l_(419173)

except ImportError:
    pass
try:
    from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
    _l_(419175)

except ImportError:
    pass
try:
    from sqlalchemy.orm import relationship
    _l_(419177)

except ImportError:
    pass

class User(_n_(419178, "Base", lambda: Base)):
    _l_(419203)

    __tablename__  = "users"
    _l_(419179)

    id = _c_(419182, _n_(419180, "Column", lambda: Column), _n_(419181, "Integer", lambda: Integer), primary_key=True, index=True)
    _l_(419183)
    username = _c_(419186, _n_(419184, "Column", lambda: Column), _n_(419185, "String", lambda: String), unique=True, index=True)
    _l_(419187)
    email = _c_(419190, _n_(419188, "Column", lambda: Column), _n_(419189, "String", lambda: String), unique=True, index=True)
    _l_(419191)
    password = _c_(419194, _n_(419192, "Column", lambda: Column), _n_(419193, "String", lambda: String))
    _l_(419195)
    is_active = _c_(419198, _n_(419196, "Column", lambda: Column), _n_(419197, "Boolean", lambda: Boolean), default=True)
    _l_(419199)

    todo = _c_(419201, _n_(419200, "relationship", lambda: relationship), "Todo", back_populates="owner")
    _l_(419202)

class Todo(_n_(419204, "Base", lambda: Base)):
    _l_(419227)

    __tablename__ = "todo"
    _l_(419205)

    id = _c_(419208, _n_(419206, "Column", lambda: Column), _n_(419207, "Integer", lambda: Integer), primary_key=True, index=True)
    _l_(419209)
    title = _c_(419212, _n_(419210, "Column", lambda: Column), _n_(419211, "String", lambda: String), index=True)
    _l_(419213)
    description = _c_(419216, _n_(419214, "Column", lambda: Column), _n_(419215, "String", lambda: String), index=True)
    _l_(419217)
    owner_id = _c_(419222, _n_(419218, "Column", lambda: Column), _n_(419219, "Integer", lambda: Integer), _c_(419221, _n_(419220, "ForeignKey", lambda: ForeignKey), "users.id"))
    _l_(419223)

    owner = _c_(419225, _n_(419224, "relationship", lambda: relationship), "User", back_populates="todo")
    _l_(419226)