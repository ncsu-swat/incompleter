# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68329046/fastapi-attributeerror-job-board-object-has-no-attribute-query
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sqlalchemy.orm import Session
    _l_(594208)

except ImportError:
    pass
try:
    from schemas.users import UserCreate
    _l_(594210)

except ImportError:
    pass
try:
    from schemas.jobs import JobCreate
    _l_(594212)

except ImportError:
    pass
try:
    from db.models.users import User
    _l_(594214)

except ImportError:
    pass
try:
    from db.models.jobs import Job
    _l_(594216)

except ImportError:
    pass
try:
    from core.hashing import Hasher
    _l_(594218)

except ImportError:
    pass



class job_board():
    _l_(594291)

    def __init__(self, db_session: _n_(594219, "Session", lambda: Session)):
        _l_(594223)

        _n_(594220, "self", lambda: self).db_session = _n_(594221, "db_session", lambda: db_session)
        _l_(594222)

    async def register_user(self, user: _n_(594224, "UserCreate", lambda: UserCreate)):
        _l_(594250)

        new_user = _c_(594235, _n_(594225, "User", lambda: User), username=_a_(594227, _n_(594226, "user", lambda: user), "username"),
        email=_a_(594229, _n_(594228, "user", lambda: user), "email"),
        hashed_password=_c_(594234, _a_(594231, _n_(594230, "Hasher", lambda: Hasher), "get_password_hash"), _a_(594233, _n_(594232, "user", lambda: user), "password")),
        is_active = False,
        is_superuser=False
        )
        _l_(594236)
        _c_(594241, _a_(594239, _a_(594238, _n_(594237, "self", lambda: self), "db_session"), "add"), _n_(594240, "new_user", lambda: new_user))
        _l_(594242)
        await _c_(594246, _a_(594245, _a_(594244, _n_(594243, "self", lambda: self), "db_session"), "flush"))
        _l_(594247)
        aux = _n_(594248, "new_user", lambda: new_user)
        _l_(594249)
        return aux

    
    async def create_new_job(self, job: _n_(594251, "JobCreate", lambda: JobCreate), owner_id: _n_(594252, "int", lambda: int)):
        _l_(594273)

        new_job = _c_(594258, _n_(594253, "Job", lambda: Job), **_c_(594256, _a_(594255, _n_(594254, "job", lambda: job), "dict")), owner_id = _n_(594257, "owner_id", lambda: owner_id))
        _l_(594259)
        _c_(594264, _a_(594262, _a_(594261, _n_(594260, "self", lambda: self), "db_session"), "add"), _n_(594263, "new_job", lambda: new_job))
        _l_(594265)
        await _c_(594269, _a_(594268, _a_(594267, _n_(594266, "self", lambda: self), "db_session"), "flush"))
        _l_(594270)
        aux = _n_(594271, "new_job", lambda: new_job)
        _l_(594272)
        return aux

    def retrieve_job(db: _n_(594274, "Session", lambda: Session), id:_n_(594275, "int", lambda: int)):
        _l_(594290)

        item = _c_(594286, _a_(594285, _c_(594284, _a_(594280, _c_(594279, _a_(594277, _n_(594276, "db", lambda: db), "query"), _n_(594278, "Job", lambda: Job)), "filter"), _a_(594282, _n_(594281, "Job", lambda: Job), "id") == _n_(594283, "id", lambda: id)), "first"))
        _l_(594287)
        aux = _n_(594288, "item", lambda: item)
        _l_(594289)
        return aux