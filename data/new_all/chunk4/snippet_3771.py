# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68329046/fastapi-attributeerror-job-board-object-has-no-attribute-query
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from db.session import async_session
    _l_(580990)

except ImportError:
    pass
try:
    from db.repository.job_board_dal import job_board
    _l_(580992)

except ImportError:
    pass

async def get_db():
    _l_(581004)

    async with _c_(580994, _n_(580993, "async_session", lambda: async_session)) as session:
        _l_(581003)

        async with _c_(580997, _a_(580996, _n_(580995, "session", lambda: session), "begin")):
            _l_(581002)

            yield _c_(581000, _n_(580998, "job_board", lambda: job_board), _n_(580999, "session", lambda: session))
            _l_(581001)