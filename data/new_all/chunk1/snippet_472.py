# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68053973/typeerror-cannot-pickle-module-object-in-fastapi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import datetime, timedelta
    _l_(402915)

except ImportError:
    pass
try:
    from fastapi import HTTPException, status, Depends, Security
    _l_(402917)

except ImportError:
    pass
try:
    from fastapi.security.oauth2 import OAuth2PasswordBearer, OAuth2PasswordRequestForm, SecurityScopes
    _l_(402919)

except ImportError:
    pass
try:
    from passlib.context import CryptContext
    _l_(402921)

except ImportError:
    pass
try:
    from jose import JWTError, jwt
    _l_(402923)

except ImportError:
    pass
try:
    from pydantic import ValidationError
    _l_(402925)

except ImportError:
    pass
try:
    from sqlalchemy.orm import Session
    _l_(402927)

except ImportError:
    pass
try:
    from ..models.user_model import User
    _l_(402929)

except ImportError:
    pass
try:
    from ..schemas import token_schema
    _l_(402931)

except ImportError:
    pass
try:
    from ..config.config import get_configurations
    _l_(402933)

except ImportError:
    pass
try:
    from ..config.database import get_db
    _l_(402935)

except ImportError:
    pass

c = _c_(402937, _n_(402936, "get_configurations", lambda: get_configurations))
_l_(402938)
SECRET_KEY = _a_(402940, _n_(402939, "c", lambda: c), "secret_key")
_l_(402941)
HASH_ALGORITHM = _a_(402943, _n_(402942, "c", lambda: c), "hash_algorithm")
_l_(402944)
ACCESS_TOKEN_EXPIRE_MINUTES = _a_(402946, _n_(402945, "c", lambda: c), "access_token_expire_minutes")
_l_(402947)

pwd_context = _c_(402949, _n_(402948, "CryptContext", lambda: CryptContext), schemes=["bcrypt"], deprecated="auto")
_l_(402950)
oauth2_scheme = _c_(402952, _n_(402951, "OAuth2PasswordBearer", lambda: OAuth2PasswordBearer), tokenUrl="token",
    scopes={"userinfo": "gg"}
)
_l_(402953)

def verify_password(plain, hashed):
    _l_(402960)

    aux = _c_(402958, _a_(402955, _n_(402954, "pwd_context", lambda: pwd_context), "verify"), _n_(402956, "plain", lambda: plain), _n_(402957, "hashed", lambda: hashed))
    _l_(402959)
    return aux

def get_hashed_password(plain):
    _l_(402966)

    aux = _c_(402964, _a_(402962, _n_(402961, "pwd_context", lambda: pwd_context), "hash"), _n_(402963, "plain", lambda: plain))
    _l_(402965)
    return aux

def is_authenticated_user(form_data: _n_(402967, "OAuth2PasswordRequestForm", lambda: OAuth2PasswordRequestForm), db: _n_(402968, "Session", lambda: Session) = _c_(402970, _n_(402969, "get_db", lambda: get_db))):
    _l_(402996)

    user = _c_(402982, _a_(402981, _c_(402980, _a_(402975, _c_(402974, _a_(402972, _n_(402971, "db", lambda: db), "query"), _n_(402973, "User", lambda: User)), "filter"), _a_(402977, _n_(402976, "User", lambda: User), "email") == _a_(402979, _n_(402978, "form_data", lambda: form_data), "username")), "first"))
    _l_(402983)

    if not _n_(402984, "user", lambda: user) or \
        not _c_(402991, _n_(402985, "verify_password", lambda: verify_password), _a_(402987, _n_(402986, "form_data", lambda: form_data), "password"), _a_(402990, _a_(402989, _n_(402988, "user", lambda: user), "password"), "password_history")[-1]):
        _l_(402993)

        aux = False
        _l_(402992)
        return aux
    aux = _n_(402994, "user", lambda: user)    
    _l_(402995)    
    return aux    

def create_access_token(data: _n_(402997, "dict", lambda: dict), expire_minutes: _n_(402998, "int", lambda: int) = _n_(402999, "ACCESS_TOKEN_EXPIRE_MINUTES", lambda: ACCESS_TOKEN_EXPIRE_MINUTES)):
    _l_(403023)

    to_encode = _c_(403002, _a_(403001, _n_(403000, "data", lambda: data), "copy"))
    _l_(403003)
    _c_(403012, _a_(403005, _n_(403004, "to_encode", lambda: to_encode), "update"), {"exp": _c_(403008, _a_(403007, _n_(403006, "datetime", lambda: datetime), "utcnow")) + _c_(403011, _n_(403009, "timedelta", lambda: timedelta), minutes=_n_(403010, "expire_minutes", lambda: expire_minutes))})
    _l_(403013)

    encoded_jwt = _c_(403019, _a_(403015, _n_(403014, "jwt", lambda: jwt), "encode"), _n_(403016, "to_encode", lambda: to_encode), _n_(403017, "SECRET_KEY", lambda: SECRET_KEY), algorithm=_n_(403018, "HASH_ALGORITHM", lambda: HASH_ALGORITHM))
    _l_(403020)
    aux = _n_(403021, "encoded_jwt", lambda: encoded_jwt)
    _l_(403022)
    return aux

async def get_current_user(security_scopes: _n_(403024, "SecurityScopes", lambda: SecurityScopes), token: _n_(403025, "str", lambda: str) = _c_(403028, _n_(403026, "Depends", lambda: Depends), _n_(403027, "oauth2_scheme", lambda: oauth2_scheme)), db: _n_(403029, "Session", lambda: Session) = _c_(403031, _n_(403030, "get_db", lambda: get_db))):
    _l_(403106)

    authenticate_value = "Bearer" \
            + f' scope="{_a_(403033, _n_(403032, "security_scopes", lambda: security_scopes), "scope_str")}"' if _a_(403035, _n_(403034, 'security_scopes', lambda: security_scopes), 'scopes') else ''
    _l_(403036)

    credentials_exception = _c_(403041, _n_(403037, 'HTTPException', lambda: HTTPException), status_code=_a_(403039, _n_(403038, 'status', lambda: status), 'HTTP_401_UNAUTHORIZED'),
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": _n_(403040, 'authenticate_value', lambda: authenticate_value)}
    )
    _l_(403042)

    try:
        _l_(403074)

        payload = _c_(403048, _a_(403044, _n_(403043, 'jwt', lambda: jwt), 'decode'), _n_(403045, 'token', lambda: token), _n_(403046, 'SECRET_KEY', lambda: SECRET_KEY), algorithms=[_n_(403047, 'HASH_ALGORITHM', lambda: HASH_ALGORITHM)])
        _l_(403049)
        email: _n_(403050, 'str', lambda: str) = _c_(403053, _a_(403052, _n_(403051, 'payload', lambda: payload), 'get'), "email")
        _l_(403054)

        if not _n_(403055, 'email', lambda: email):
            _l_(403058)

            raise _n_(403056, 'credentials_exception', lambda: credentials_exception)
            _l_(403057)

        token_scopes = _c_(403061, _a_(403060, _n_(403059, 'payload', lambda: payload), 'get'), "scopes", [])
        _l_(403062)
        token_data = _c_(403067, _a_(403064, _n_(403063, 'token_schema', lambda: token_schema), 'TokenData'), email=_n_(403065, 'email', lambda: email), scopes=_n_(403066, 'token_scopes', lambda: token_scopes))
        _l_(403068)
    except (_n_(403069, 'JWTError', lambda: JWTError), _n_(403070, 'ValidationError', lambda: ValidationError)):
        _l_(403073)

        raise _n_(403071, 'credentials_exception', lambda: credentials_exception)
        _l_(403072)

    user = _c_(403085, _a_(403084, _c_(403083, _a_(403079, _c_(403078, _a_(403076, _n_(403075, 'db', lambda: db), 'query'), _n_(403077, 'User', lambda: User)), 'filter'), _a_(403081, _n_(403080, 'User', lambda: User), 'email') == _n_(403082, 'email', lambda: email)), 'first'))
    _l_(403086)
    if not _n_(403087, 'user', lambda: user):
        _l_(403090)

        raise _n_(403088, 'credentials_exception', lambda: credentials_exception)
        _l_(403089)

    for scope in _a_(403092, _n_(403091, 'security_scopes', lambda: security_scopes), 'scopes'):
        _l_(403103)

        if _n_(403093, 'scope', lambda: scope) not in _a_(403095, _n_(403094, 'token_data', lambda: token_data), 'scopes'):
            _l_(403102)

            raise _c_(403100, _n_(403096, 'HTTPException', lambda: HTTPException), status_code=_a_(403098, _n_(403097, 'status', lambda: status), 'HTTP_401_UNAUTHORIZED'),
                detail="Not enough permissions",
                headers={"WWW-Authenticate": _n_(403099, 'authenticate_value', lambda: authenticate_value)}
            )
            _l_(403101)
    aux = _n_(403104, 'user', lambda: user)
    _l_(403105)

    return aux

async def get_current_active_user(current_user: _n_(403107, 'User', lambda: User) = _c_(403110, _n_(403108, 'Security', lambda: Security), _n_(403109, 'get_current_user', lambda: get_current_user), scopes=[])):
    _l_(403120)

    if not _n_(403111, 'current_user', lambda: current_user):
        _l_(403117)

        raise _c_(403115, _n_(403112, 'HTTPException', lambda: HTTPException), status_code=_a_(403114, _n_(403113, 'status', lambda: status), 'HTTP_400_BAD_REQUEST'), detail="Inactive user")
        _l_(403116)
    aux = _n_(403118, 'current_user', lambda: current_user)
    _l_(403119)
    return aux