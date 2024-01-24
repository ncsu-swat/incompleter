# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68330275/fastapi-typeerror-retreive-job-got-multiple-values-for-argument-id
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from fastapi import APIRouter, HTTPException, status
    _l_(544370)

except ImportError:
    pass
try:
    from fastapi import Depends
    _l_(544372)

except ImportError:
    pass
try:
    from db.repository.job_board_dal import job_board
    _l_(544374)

except ImportError:
    pass
try:
    from schemas.jobs import JobCreate, ShowJob
    _l_(544376)

except ImportError:
    pass
try:
    from db.repository.job_board_dal import Job
    _l_(544378)

except ImportError:
    pass
try:
    from depends import get_db
    _l_(544380)

except ImportError:
    pass

router = _c_(544382, _n_(544381, "APIRouter", lambda: APIRouter))
_l_(544383)

@_c_(544387, _a_(544385, _n_(544384, "router", lambda: router), "post"), "/create-job",response_model=_n_(544386, "ShowJob", lambda: ShowJob))
async def create_user(Job: _n_(544388, "JobCreate", lambda: JobCreate), jobs: _n_(544389, "Job", lambda: Job) = _c_(544392, _n_(544390, "Depends", lambda: Depends), _n_(544391, "get_db", lambda: get_db))):
    _l_(544400)

    owner_id = 1
    _l_(544393)
    aux = await _c_(544398, _a_(544395, _n_(544394, "jobs", lambda: jobs), "create_new_job"), _n_(544396, "Job", lambda: Job), _n_(544397, "owner_id", lambda: owner_id))
    _l_(544399)
    return aux

@_c_(544403, _a_(544402, _n_(544401, "router", lambda: router), "get"), "/get/{id}")
def retrieve_job_by_id(id:_n_(544404, "int", lambda: int), job_board = _c_(544407, _n_(544405, "Depends", lambda: Depends), _n_(544406, "get_db", lambda: get_db))):
    _l_(544424)

    #print(type(session))
    job_id = _c_(544412, _a_(544409, _n_(544408, "job_board", lambda: job_board), "retrieve_job"), _n_(544410, "job_board", lambda: job_board), id=_n_(544411, "id", lambda: id))
    _l_(544413)
    if not _n_(544414, "job_id", lambda: job_id):
        _l_(544421)

        _c_(544419, _n_(544415, "HTTPException", lambda: HTTPException), status_code=_a_(544417, _n_(544416, "status", lambda: status), "HTTP_404_NOT_FOUND"),
        detail=f"Job with id {_n_(544418, 'id', lambda: id)} does not exist")
        _l_(544420)
    aux = _n_(544422, "job_id", lambda: job_id)
    _l_(544423)
    return aux