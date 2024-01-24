# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71012290/switching-to-routers-in-fastapi-did-not-go-well-response-model-list-pydantic
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import models
    _l_(538187)

except ImportError:
    pass
try:
    from database import get_db
    _l_(538189)

except ImportError:
    pass

router: _n_(538190, "APIRouter", lambda: APIRouter) = _c_(538192, _n_(538191, "APIRouter", lambda: APIRouter))
_l_(538193)


@_c_(538199, _a_(538195, _n_(538194, "router", lambda: router), "get"), "/postss", response_model=_n_(538196, "List", lambda: List)[_a_(538198, _n_(538197, "models", lambda: models), "Post")])
def get_post(db: _n_(538200, "Session", lambda: Session) = _c_(538203, _n_(538201, "Depends", lambda: Depends), _n_(538202, "get_db", lambda: get_db))):
    _l_(538226)

    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    # print(posts)

    try:
        _l_(538223)

        posts = _c_(538210, _a_(538209, _c_(538208, _a_(538205, _n_(538204, "db", lambda: db), "query"), _a_(538207, _n_(538206, "models", lambda: models), "Post")), "all"))
        _l_(538211)
    except _n_(538212, "Exception", lambda: Exception) as ex:
        _l_(538222)

        msg = f"Unexpected {_n_(538213, 'ex', lambda: ex)=}, {_c_(538216, _n_(538214, 'type', lambda: type), _n_(538215, 'ex', lambda: ex))=}"
        _l_(538217)
        raise _c_(538220, _n_(538218, "HTTPException", lambda: HTTPException), status_code=500, detail=_n_(538219, "msg", lambda: msg))
        _l_(538221)
    aux = _n_(538224, "posts", lambda: posts)
    _l_(538225)
    return aux