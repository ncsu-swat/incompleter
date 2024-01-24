# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68330275/fastapi-typeerror-retreive-job-got-multiple-values-for-argument-id
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(550145, _a_(550144, _n_(550143, "router", lambda: router), "get"), "/get/{id}")
def retrieve_job_by_id(id:_n_(550146, "int", lambda: int), id_job: _n_(550147, "job_board", lambda: job_board) = _c_(550150, _n_(550148, "Depends", lambda: Depends), _n_(550149, "get_db", lambda: get_db))):
    _l_(550167)

    #print(type(session))
    job_id = _c_(550155, _a_(550152, _n_(550151, "job_board", lambda: job_board), "retrieve_job"), _n_(550153, "id_job", lambda: id_job), id=_n_(550154, "id", lambda: id))
    _l_(550156)
    if not _n_(550157, "job_id", lambda: job_id):
        _l_(550164)

        _c_(550162, _n_(550158, "HTTPException", lambda: HTTPException), status_code=_a_(550160, _n_(550159, "status", lambda: status), "HTTP_404_NOT_FOUND"),
        detail=f"Job with id {_n_(550161, 'id', lambda: id)} does not exist")
        _l_(550163)
    aux = _n_(550165, "job_id", lambda: job_id)
    _l_(550166)
    return aux