# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68330275/fastapi-typeerror-retreive-job-got-multiple-values-for-argument-id
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sqlalchemy.orm import Session, query
    _l_(540197)

except ImportError:
    pass
try:
    from schemas.users import UserCreate
    _l_(540199)

except ImportError:
    pass
try:
    from schemas.jobs import JobCreate
    _l_(540201)

except ImportError:
    pass
try:
    from db.models.users import User
    _l_(540203)

except ImportError:
    pass
try:
    from db.models.jobs import Job
    _l_(540205)

except ImportError:
    pass
try:
    from core.hashing import Hasher
    _l_(540207)

except ImportError:
    pass



class job_board():
    _l_(540280)

    def __init__(self, db_session: _n_(540208, "Session", lambda: Session)):
        _l_(540212)

        _n_(540209, "self", lambda: self).db_session = _n_(540210, "db_session", lambda: db_session)
        _l_(540211)

    async def register_user(self, user: _n_(540213, "UserCreate", lambda: UserCreate)):
        _l_(540239)

        new_user = _c_(540224, _n_(540214, "User", lambda: User), username=_a_(540216, _n_(540215, "user", lambda: user), "username"),
        email=_a_(540218, _n_(540217, "user", lambda: user), "email"),
        hashed_password=_c_(540223, _a_(540220, _n_(540219, "Hasher", lambda: Hasher), "get_password_hash"), _a_(540222, _n_(540221, "user", lambda: user), "password")),
        is_active = False,
        is_superuser=False
        )
        _l_(540225)
        _c_(540230, _a_(540228, _a_(540227, _n_(540226, "self", lambda: self), "db_session"), "add"), _n_(540229, "new_user", lambda: new_user))
        _l_(540231)
        await _c_(540235, _a_(540234, _a_(540233, _n_(540232, "self", lambda: self), "db_session"), "flush"))
        _l_(540236)
        aux = _n_(540237, "new_user", lambda: new_user)
        _l_(540238)
        return aux

    
    async def create_new_job(self, job: _n_(540240, "JobCreate", lambda: JobCreate), owner_id: _n_(540241, "int", lambda: int)):
        _l_(540262)

        new_job = _c_(540247, _n_(540242, "Job", lambda: Job), **_c_(540245, _a_(540244, _n_(540243, "job", lambda: job), "dict")), owner_id = _n_(540246, "owner_id", lambda: owner_id))
        _l_(540248)
        _c_(540253, _a_(540251, _a_(540250, _n_(540249, "self", lambda: self), "db_session"), "add"), _n_(540252, "new_job", lambda: new_job))
        _l_(540254)
        await _c_(540258, _a_(540257, _a_(540256, _n_(540255, "self", lambda: self), "db_session"), "flush"))
        _l_(540259)
        aux = _n_(540260, "new_job", lambda: new_job)
        _l_(540261)
        return aux

    def retrieve_job(self, id:_n_(540263, "int", lambda: int)):
        _l_(540279)

        item = _c_(540275, _a_(540274, _c_(540273, _a_(540269, _c_(540268, _a_(540266, _a_(540265, _n_(540264, "self", lambda: self), "db_session"), "query"), _n_(540267, "Job", lambda: Job)), "filter"), _a_(540271, _n_(540270, "Job", lambda: Job), "id") == _n_(540272, "id", lambda: id)), "first"))
        _l_(540276)
        aux = _n_(540277, "item", lambda: item)
        _l_(540278)
        return aux