from fastapi import APIRouter, status, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.database import get_db
from app.repositories.task import TaskRepository
from app.schemas.task import TaskStatus, TaskCreate, TaskListResponse, TaskResponse, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def createTask(task: TaskCreate, db: Session = Depends(get_db)):
    try:
        task_repo = TaskRepository(db)
        return task_repo.create(task)
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    

@router.get("/", response_model=TaskListResponse)
def listTasks(skip:int = Query(0, ge=0), limit: int = Query(10, ge=1, le=100), 
              status_filter: TaskStatus = Query(None, alias="status"), db: Session = Depends(get_db)):
    repo = TaskRepository(db)
    items, total = repo.get_all(skip=skip, limit=limit, status_filter=status_filter)

    return TaskListResponse(total=total, skip=skip, limit=limit, items=items)

@router.get("/{task_id}", response_model=TaskResponse)
def getTask(task_id: int, db: Session=Depends(get_db)):
    task_repo = TaskRepository(db)
    db_task = task_repo.get_by_id(task_id)
    if not db_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Task id:{task_id} not found")
    return db_task

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)):
    try:
        repo = TaskRepository(db)
        db_task = repo.update(task_id, task_update)
        if not db_task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail=f"task id {task_id} not found"
            )
        return db_task
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="title already exists"
        )
    
@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    """Delete a task"""
    repo = TaskRepository(db)
    success = repo.delete(task_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f"task id {task_id} not found"
        )
    return None