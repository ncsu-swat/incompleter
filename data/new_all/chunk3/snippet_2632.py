# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68330275/fastapi-typeerror-retreive-job-got-multiple-values-for-argument-id
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from db.session import async_session
    _l_(565787)

except ImportError:
    pass
try:
    from db.repository.job_board_dal import job_board
    _l_(565789)

except ImportError:
    pass

async def get_db():
    _l_(565801)

    async with _c_(565791, _n_(565790, "async_session", lambda: async_session)) as session:
        _l_(565800)

        async with _c_(565794, _a_(565793, _n_(565792, "session", lambda: session), "begin")):
            _l_(565799)

            yield _c_(565797, _n_(565795, "job_board", lambda: job_board), _n_(565796, "session", lambda: session))
            _l_(565798)