# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71012290/switching-to-routers-in-fastapi-did-not-go-well-response-model-list-pydantic
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import datetime
    _l_(553168)

except ImportError:
    pass
try:
    from pydantic import BaseModel, EmailStr
    _l_(553170)

except ImportError:
    pass


class PostBase(_n_(553171, "BaseModel", lambda: BaseModel)):
    _l_(553178)

    title: _n_(553172, "str", lambda: str)
    _l_(553173)
    content: _n_(553174, "str", lambda: str)
    _l_(553175)
    published: _n_(553176, "bool", lambda: bool) = True
    _l_(553177)


class PostCreate(_n_(553179, "BaseModel", lambda: BaseModel)):
    _l_(553181)

    pass
    _l_(553180)


class Post(_n_(553182, "PostBase", lambda: PostBase)):
    _l_(553190)

    id: _n_(553183, "int", lambda: int)
    _l_(553184)
    created_at: _n_(553185, "datetime", lambda: datetime)
    _l_(553186)

    class Config:
        _l_(553189)

        orm_mode = True
        _l_(553187)
        arbitrary_types_allowed = True
        _l_(553188)


class UserCreate(_n_(553191, "BaseModel", lambda: BaseModel)):
    _l_(553196)

    email: _n_(553192, "EmailStr", lambda: EmailStr)
    _l_(553193)
    password: _n_(553194, "str", lambda: str)
    _l_(553195)


class UserOut(_n_(553197, "BaseModel", lambda: BaseModel)):
    _l_(553206)

    id: _n_(553198, "int", lambda: int)
    _l_(553199)
    email: _n_(553200, "EmailStr", lambda: EmailStr)
    _l_(553201)
    created_at: _n_(553202, "datetime", lambda: datetime)
    _l_(553203)

    class Config:
        _l_(553205)

        orm_mode = True
        _l_(553204)