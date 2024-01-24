# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64236572/fastapi-typeerror-object-of-type-modelmetaclass-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from typing import List, Optional
    _l_(383774)

except ImportError:
    pass
try:
    from pydantic import BaseModel
    _l_(383776)

except ImportError:
    pass


# Todo model
class TodoBase(_n_(383777, "BaseModel", lambda: BaseModel)):
    _l_(383783)

    title: _n_(383778, "str", lambda: str)
    _l_(383779)
    description: _n_(383780, "Optional", lambda: Optional)[_n_(383781, "str", lambda: str)] = None
    _l_(383782)

class TodoCreation(_n_(383784, "TodoBase", lambda: TodoBase)):
    _l_(383786)

    pass
    _l_(383785)


class Todo(_n_(383787, "TodoBase", lambda: TodoBase)):
    _l_(383794)

    id: _n_(383788, "int", lambda: int)
    _l_(383789)
    owner_id: _n_(383790, "int", lambda: int)
    _l_(383791)

    class Config:
        _l_(383793)

        orm_mode = True
        _l_(383792)
# User model
class UserBase(_n_(383795, "BaseModel", lambda: BaseModel)):
    _l_(383800)

    username: _n_(383796, "str", lambda: str)
    _l_(383797)
    email: _n_(383798, "str", lambda: str)
    _l_(383799)

class UserCreation(_n_(383801, "UserBase", lambda: UserBase)):
    _l_(383804)

    password: _n_(383802, "str", lambda: str)
    _l_(383803)

class User(_n_(383805, "UserBase", lambda: UserBase)):
    _l_(383815)

    id: _n_(383806, "int", lambda: int)
    _l_(383807)
    is_active: _n_(383808, "bool", lambda: bool)
    _l_(383809)
    todo: _n_(383810, "List", lambda: List)[_n_(383811, "Todo", lambda: Todo)] = []
    _l_(383812)

    class Config:
        _l_(383814)

        orm_mode = True
        _l_(383813)