#Source: https://stackoverflow.com/questions/68329046/fastapi-attributeerror-job-board-object-has-no-attribute-query
from db.session import async_session
from db.repository.job_board_dal import job_board

async def get_db():
    async with async_session() as session:
        async with session.begin():
            yield job_board(session)