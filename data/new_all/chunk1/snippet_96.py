# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64236572/fastapi-typeerror-object-of-type-modelmetaclass-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from typing import List
    _l_(377740)

except ImportError:
    pass
try:
    from fastapi import FastAPI, Depends, HTTPException, status
    _l_(377742)

except ImportError:
    pass
try:
    from sqlalchemy.orm import Session
    _l_(377744)

except ImportError:
    pass
try:
    from sql import crud, database, sql_models
    _l_(377746)

except ImportError:
    pass
try:
    from pydantic_models import User, Todo, UserCreation, TodoCreation
    _l_(377748)

except ImportError:
    pass


_c_(377755, _a_(377752, _a_(377751, _a_(377750, _n_(377749, "sql_models", lambda: sql_models), "Base"), "metadata"), "create_all"), bind=_a_(377754, _n_(377753, "database", lambda: database), "engine"))
_l_(377756)

app = _c_(377758, _n_(377757, "FastAPI", lambda: FastAPI))
_l_(377759)

def get_db():
    _l_(377772)

    db = _c_(377762, _a_(377761, _n_(377760, "database", lambda: database), "SessionLocal"))
    _l_(377763)
    try:
        _l_(377771)

        yield _n_(377764, "db", lambda: db)
        _l_(377765)
    finally:
        _l_(377770)

        _c_(377768, _a_(377767, _n_(377766, "db", lambda: db), "close"))
        _l_(377769)


@_c_(377776, _a_(377774, _n_(377773, "app", lambda: app), "post"), "/users/", response_model=_n_(377775, "User", lambda: User))
def create_user(user=_n_(377777, "User", lambda: User), db: _n_(377778, "Session", lambda: Session) = _c_(377781, _n_(377779, "Depends", lambda: Depends), _n_(377780, "get_db", lambda: get_db))):
    _l_(377805)

    db_user_email = _c_(377787, _a_(377783, _n_(377782, "crud", lambda: crud), "get_user_by_email"), _n_(377784, "db", lambda: db), email=_a_(377786, _n_(377785, "user", lambda: user), "email"))
    _l_(377788)
    db_user_name = _a_(377790, _n_(377789, "crud", lambda: crud), "get_user")
    _l_(377791)
    if _n_(377792, "db_user", lambda: db_user):
        _l_(377798)

        raise _c_(377796, _n_(377793, "HTTPException", lambda: HTTPException), status_code=_a_(377795, _n_(377794, "status", lambda: status), "HTTP_400_BAD"),
                            detail="Email already taken")
        _l_(377797)
    aux = _c_(377803, _a_(377800, _n_(377799, "crud", lambda: crud), "create_user"), db=_n_(377801, "db", lambda: db), user=_n_(377802, "user", lambda: user))
    _l_(377804)
    return aux


@_c_(377810, _a_(377807, _n_(377806, "app", lambda: app), "get"), "/users/", response_model=_n_(377808, "List", lambda: List)[_n_(377809, "User", lambda: User)])
def read_all_users(skip: _n_(377811, "int", lambda: int) = 0, limit: _n_(377812, "int", lambda: int) = 100, db: _n_(377813, "Session", lambda: Session) = _c_(377816, _n_(377814, "Depends", lambda: Depends), _n_(377815, "get_db", lambda: get_db))):
    _l_(377826)

    users = _c_(377822, _a_(377818, _n_(377817, "crud", lambda: crud), "get_all_users"), _n_(377819, "db", lambda: db), skip=_n_(377820, "skip", lambda: skip), limit=_n_(377821, "limit", lambda: limit))
    _l_(377823)
    aux = _n_(377824, "users", lambda: users)
    _l_(377825)
    return aux


@_c_(377830, _a_(377828, _n_(377827, "app", lambda: app), "get"), "/users/{user_id}", response_model=_n_(377829, "User", lambda: User))
def read_user(user_id: _n_(377831, "int", lambda: int), db: _n_(377832, "Session", lambda: Session) = _c_(377835, _n_(377833, "Depends", lambda: Depends), _n_(377834, "get_db", lambda: get_db))):
    _l_(377851)

    db_user = _c_(377840, _a_(377837, _n_(377836, "crud", lambda: crud), "get_user"), _n_(377838, "db", lambda: db), user_id=_n_(377839, "user_id", lambda: user_id))
    _l_(377841)
    if _n_(377842, "db_user", lambda: db_user) is None:
        _l_(377848)

        raise _c_(377846, _n_(377843, "HTTPException", lambda: HTTPException), status_code=_a_(377845, _n_(377844, "status", lambda: status), "HTTP_404_NOT_FOUND"), detail="User not found")
        _l_(377847)
    aux = _n_(377849, "db_user", lambda: db_user)
    _l_(377850)
    return aux


@_c_(377855, _a_(377853, _n_(377852, "app", lambda: app), "post"), "/users/{user_id}/todo/", response_model=_n_(377854, "Todo", lambda: Todo))
def create_todo_list(user_id: _n_(377856, "int", lambda: int), todo: _n_(377857, "TodoCreation", lambda: TodoCreation), db: _n_(377858, "Session", lambda: Session) = _c_(377861, _n_(377859, "Depends", lambda: Depends), _n_(377860, "get_db", lambda: get_db))):
    _l_(377869)

    aux = _c_(377867, _a_(377863, _n_(377862, "crud", lambda: crud), "create_todo"), db=_n_(377864, "db", lambda: db), todo=_n_(377865, "todo", lambda: todo), user_id=_n_(377866, "user_id", lambda: user_id))
    _l_(377868)
    return aux


@_c_(377874, _a_(377871, _n_(377870, "app", lambda: app), "get"), "/items/", response_model=_n_(377872, "List", lambda: List)[_n_(377873, "Todo", lambda: Todo)])
def read_todo(skip: _n_(377875, "int", lambda: int) = 0, limit: _n_(377876, "int", lambda: int) = 100, db: _n_(377877, "Session", lambda: Session) = _c_(377880, _n_(377878, "Depends", lambda: Depends), _n_(377879, "get_db", lambda: get_db))):
    _l_(377890)

    todos = _c_(377886, _a_(377882, _n_(377881, "crud", lambda: crud), "get_todo"), _n_(377883, "db", lambda: db), skip=_n_(377884, "skip", lambda: skip), limit=_n_(377885, "limit", lambda: limit))
    _l_(377887)
    aux = _n_(377888, "todos", lambda: todos)
    _l_(377889)
    return aux