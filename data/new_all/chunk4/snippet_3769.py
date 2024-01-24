# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68329046/fastapi-attributeerror-job-board-object-has-no-attribute-query
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from fastapi import APIRouter, HTTPException, status
    _l_(620079)

except ImportError:
    pass
try:
    from fastapi import Depends
    _l_(620081)

except ImportError:
    pass
try:
    from sqlalchemy.orm.session import Session
    _l_(620083)

except ImportError:
    pass
try:
    from db.repository.job_board_dal import job_board
    _l_(620085)

except ImportError:
    pass
try:
    from db.models.jobs import Job as model_job
    _l_(620087)

except ImportError:
    pass
try:
    from schemas.jobs import JobCreate, ShowJob
    _l_(620089)

except ImportError:
    pass
try:
    from db.repository.job_board_dal import Job
    _l_(620091)

except ImportError:
    pass
try:
    from depends import get_db
    _l_(620093)

except ImportError:
    pass

router = _c_(620095, _n_(620094, "APIRouter", lambda: APIRouter))
_l_(620096)

@_c_(620100, _a_(620098, _n_(620097, "router", lambda: router), "post"), "/create-job",response_model=_n_(620099, "ShowJob", lambda: ShowJob))
async def create_user(Job: _n_(620101, "JobCreate", lambda: JobCreate), jobs: _n_(620102, "Job", lambda: Job) = _c_(620105, _n_(620103, "Depends", lambda: Depends), _n_(620104, "get_db", lambda: get_db))):
    _l_(620113)

    owner_id = 1
    _l_(620106)
    aux = await _c_(620111, _a_(620108, _n_(620107, "jobs", lambda: jobs), "create_new_job"), _n_(620109, "Job", lambda: Job), _n_(620110, "owner_id", lambda: owner_id))
    _l_(620112)
    return aux

@_c_(620116, _a_(620115, _n_(620114, "router", lambda: router), "get"), "/get/{id}")
def retreive_job_by_id(id:_n_(620117, "int", lambda: int), session: _n_(620118, "Session", lambda: Session) = _c_(620121, _n_(620119, "Depends", lambda: Depends), _n_(620120, "get_db", lambda: get_db))):
    _l_(620138)

    #print(type(session))
    job_id = _c_(620126, _a_(620123, _n_(620122, "job_board", lambda: job_board), "retrieve_job"), _n_(620124, "session", lambda: session), id=_n_(620125, "id", lambda: id))
    _l_(620127)
    if not _n_(620128, "job_id", lambda: job_id):
        _l_(620135)

        _c_(620133, _n_(620129, "HTTPException", lambda: HTTPException), status_code=_a_(620131, _n_(620130, "status", lambda: status), "HTTP_404_NOT_FOUND"),
        detail=f"Job with id {_n_(620132, 'id', lambda: id)} does not exist")
        _l_(620134)
    aux = _n_(620136, "job_id", lambda: job_id)
    _l_(620137)
    return aux