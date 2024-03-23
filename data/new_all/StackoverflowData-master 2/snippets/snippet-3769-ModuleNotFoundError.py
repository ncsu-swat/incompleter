#Source: https://stackoverflow.com/questions/68329046/fastapi-attributeerror-job-board-object-has-no-attribute-query
from fastapi import APIRouter, HTTPException, status
from fastapi import Depends
from sqlalchemy.orm.session import Session

from db.repository.job_board_dal import job_board
from db.models.jobs import Job as model_job
from schemas.jobs import JobCreate, ShowJob
from db.repository.job_board_dal import Job
from depends import get_db

router = APIRouter()

@router.post("/create-job",response_model=ShowJob)
async def create_user(Job: JobCreate, jobs: Job = Depends(get_db)):
    owner_id = 1
    return await jobs.create_new_job(Job, owner_id)

@router.get("/get/{id}")
def retreive_job_by_id(id:int, session: Session = Depends(get_db)):
    #print(type(session))
    job_id = job_board.retrieve_job(session, id=id)
    if not job_id:
        HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Job with id {id} does not exist")
    return job_id