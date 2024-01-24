# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71012290/switching-to-routers-in-fastapi-did-not-go-well-response-model-list-pydantic
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import models
    _l_(567940)

except ImportError:
    pass
try:
    import schemas
    _l_(567942)

except ImportError:
    pass
try:
    from database import engine, get_db
    _l_(567944)

except ImportError:
    pass
try:
    from sqlalchemy.orm import Session
    _l_(567946)

except ImportError:
    pass

_c_(567952, _a_(567950, _a_(567949, _a_(567948, _n_(567947, "models", lambda: models), "Base"), "metadata"), "create_all"), bind=_n_(567951, "engine", lambda: engine))
_l_(567953)


app = _c_(567955, _n_(567954, "FastAPI", lambda: FastAPI))
_l_(567956)
_c_(567961, _a_(567958, _n_(567957, "app", lambda: app), "include_router"), _a_(567960, _n_(567959, "user", lambda: user), "router"))
_l_(567962)
_c_(567967, _a_(567964, _n_(567963, "app", lambda: app), "include_router"), _a_(567966, _n_(567965, "post", lambda: post), "router"))
_l_(567968)

if _n_(567969, "__name__", lambda: __name__) == "__main__":
    _l_(567975)

    _c_(567973, _a_(567971, _n_(567970, "uvicorn", lambda: uvicorn), "run"), _n_(567972, "app", lambda: app), host="127.0.0.1", port=8000)
    _l_(567974)


@_c_(567978, _a_(567977, _n_(567976, "app", lambda: app), "get"), "/")
async def root():
    _l_(567980)

    aux = {"message": "Welcome To My Api!"}
    _l_(567979)
    return aux


@_c_(567986, _a_(567982, _n_(567981, "app", lambda: app), "get"), "/posts", response_model=_n_(567983, "List", lambda: List)[_a_(567985, _n_(567984, "schemas", lambda: schemas), "Post")])
def get_posts(db: _n_(567987, "Session", lambda: Session) = _c_(567990, _n_(567988, "Depends", lambda: Depends), _n_(567989, "get_db", lambda: get_db))):
    _l_(568013)

    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    # print(posts)

    try:
        _l_(568010)

        posts = _c_(567997, _a_(567996, _c_(567995, _a_(567992, _n_(567991, "db", lambda: db), "query"), _a_(567994, _n_(567993, "models", lambda: models), "Post")), "all"))
        _l_(567998)
    except _n_(567999, "Exception", lambda: Exception) as ex:
        _l_(568009)

        msg = f"Unexpected {_n_(568000, 'ex', lambda: ex)=}, {_c_(568003, _n_(568001, 'type', lambda: type), _n_(568002, 'ex', lambda: ex))=}"
        _l_(568004)
        raise _c_(568007, _n_(568005, "HTTPException", lambda: HTTPException), status_code=500, detail=_n_(568006, "msg", lambda: msg))
        _l_(568008)
    aux = _n_(568011, "posts", lambda: posts)
    _l_(568012)
    return aux