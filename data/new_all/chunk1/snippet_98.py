# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64236572/fastapi-typeerror-object-of-type-modelmetaclass-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sqlalchemy.orm import Session
    _l_(390325)

except ImportError:
    pass
try:
    from . import sql_models
    _l_(390327)

except ImportError:
    pass
try:
    import pydantic_models
    _l_(390329)

except ImportError:
    pass

# Get single user
def get_user(db: _n_(390330, "Session", lambda: Session), user_id: _n_(390331, "int", lambda: int)):
    _l_(390346)

    aux = _c_(390344, _a_(390343, _c_(390342, _a_(390337, _c_(390336, _a_(390333, _n_(390332, "db", lambda: db), "query"), _a_(390335, _n_(390334, "sql_models", lambda: sql_models), "User")), "filter"), _a_(390340, _a_(390339, _n_(390338, "models", lambda: models), "User"), "id") == _n_(390341, "user_id", lambda: user_id)), "first"))
    _l_(390345)
    return aux

def get_user_by_name(db: _n_(390347, "Session", lambda: Session), username: _n_(390348, "str", lambda: str)):
    _l_(390363)

    aux = _c_(390361, _a_(390360, _c_(390359, _a_(390354, _c_(390353, _a_(390350, _n_(390349, "db", lambda: db), "query"), _a_(390352, _n_(390351, "sql_models", lambda: sql_models), "User")), "filter"), _a_(390357, _a_(390356, _n_(390355, "models", lambda: models), "User"), "username") == _n_(390358, "username", lambda: username)), "first"))
    _l_(390362)
    return aux

# Get user by email
def get_user_by_email(db: _n_(390364, "Session", lambda: Session), email: _n_(390365, "str", lambda: str)):
    _l_(390380)

    aux = _c_(390378, _a_(390377, _c_(390376, _a_(390371, _c_(390370, _a_(390367, _n_(390366, "db", lambda: db), "query"), _a_(390369, _n_(390368, "sql_models", lambda: sql_models), "User")), "filter"), _a_(390374, _a_(390373, _n_(390372, "models", lambda: models), "User"), "email") == _n_(390375, "email", lambda: email)), "first"))
    _l_(390379)
    return aux

# Get all users
def get_all_users(db: _n_(390381, "Session", lambda: Session), skip: _n_(390382, "int", lambda: int) = 0, limit: _n_(390383, "int", lambda: int) = 100):
    _l_(390398)

    aux = _c_(390396, _a_(390395, _c_(390394, _a_(390392, _c_(390391, _a_(390389, _c_(390388, _a_(390385, _n_(390384, "db", lambda: db), "query"), _a_(390387, _n_(390386, "sql_models", lambda: sql_models), "User")), "offset"), _n_(390390, "skip", lambda: skip)), "limit"), _n_(390393, "limit", lambda: limit)), "all"))
    _l_(390397)
    return aux

# Create a user
def create_user(db: _n_(390399, "Session", lambda: Session), user: _a_(390401, _n_(390400, "pydantic_models", lambda: pydantic_models), "UserCreation")):
    _l_(390430)

    fake_hashed_password = _a_(390403, _n_(390402, "user", lambda: user), "password") + "fakehash" # Hashed user's password
    _l_(390404) # Hashed user's password
    db_user = _c_(390412, _a_(390406, _n_(390405, "sql_models", lambda: sql_models), "User"), username=_a_(390408, _n_(390407, "user", lambda: user), "username"), email=_a_(390410, _n_(390409, "user", lambda: user), "email"), password=_n_(390411, "fake_hashed_password", lambda: fake_hashed_password))
    _l_(390413)
    _c_(390417, _a_(390415, _n_(390414, "db", lambda: db), "add"), _n_(390416, "db_user", lambda: db_user))
    _l_(390418)
    _c_(390421, _a_(390420, _n_(390419, "db", lambda: db), "commit"))
    _l_(390422)
    _c_(390426, _a_(390424, _n_(390423, "db", lambda: db), "refresh"), _n_(390425, "db_user", lambda: db_user))
    _l_(390427)
    aux = _n_(390428, "db_user", lambda: db_user)
    _l_(390429)
    return aux


def get_todo(db: _n_(390431, "Session", lambda: Session), skip: _n_(390432, "int", lambda: int) = 0, limit: _n_(390433, "int", lambda: int) = 100):
    _l_(390448)

    aux = _c_(390446, _a_(390445, _c_(390444, _a_(390442, _c_(390441, _a_(390439, _c_(390438, _a_(390435, _n_(390434, "db", lambda: db), "query"), _a_(390437, _n_(390436, "sql_models", lambda: sql_models), "Todo")), "offset"), _n_(390440, "skip", lambda: skip)), "limit"), _n_(390443, "limit", lambda: limit)), "all"))
    _l_(390447)
    return aux


def create_todo(db: _n_(390449, "Session", lambda: Session), todo: _a_(390451, _n_(390450, "pydantic_models", lambda: pydantic_models), "TodoCreation"), user_id: _n_(390452, "int", lambda: int)):
    _l_(390477)

    db_item = _c_(390459, _a_(390454, _n_(390453, "models", lambda: models), "Item"), **_c_(390457, _a_(390456, _n_(390455, "item", lambda: item), "dict")), owner_id=_n_(390458, "user_id", lambda: user_id))
    _l_(390460)
    _c_(390464, _a_(390462, _n_(390461, "db", lambda: db), "add"), _n_(390463, "db_item", lambda: db_item))
    _l_(390465)
    _c_(390468, _a_(390467, _n_(390466, "db", lambda: db), "commit"))
    _l_(390469)
    _c_(390473, _a_(390471, _n_(390470, "db", lambda: db), "refresh"), _n_(390472, "db_item", lambda: db_item))
    _l_(390474)
    aux = _n_(390475, "db_item", lambda: db_item)
    _l_(390476)
    return aux