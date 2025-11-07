from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate
from app.constants.enums import TaskStatus

class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, task: TaskCreate) -> Task:
        try:
            db_task = Task(title=task.title, description=task.description, status=task.status)
            self.db.add(db_task)
            self.db.commit()
            self.db.refresh(db_task)
            return db_task
        except IntegrityError:
            self.db.rollback()
            raise

    def getAll(self, skip: int=0, limit: int=10, status_filter: TaskStatus=None) -> tuple[list[Task], int]:
        query = self.db.query(Task) 
        if status_filter:
            query = query.filter(Task.status == status_filter)

        total = query.count()
        items = query.offset(skip).limit(limit).all()

        return items, total

    def getById(self, task_id: int) -> Task | None:
        return self.db.query(Task).filter(Task.id == task_id).first()

    def update(self, task_id: int, task_update: TaskUpdate) -> Task | None:
        db_task = self.getById(task_id)
        if not db_task:
            return None
        
        try:
            if task_update.title is not None:
                db_task.title = task_update.title
            if task_update.description is not None:
                db_task.description = task_update.description
            if task_update.status is not None:
                db_task.status = task_update.status
            
            self.db.commit()
            self.db.refresh(db_task)
            return db_task
        except IntegrityError:
            self.db.rollback()
            raise

    def delete(self, task_id: int) -> bool:
        db_task = self.getById(task_id)
        if not db_task:
            return False
        
        self.db.delete(db_task)
        self.db.commit()
        return True
