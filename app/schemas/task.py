from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from app.constants.enums import TaskStatus

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=2000)
    status: TaskStatus = Field(default=TaskStatus.PENDING)

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=2000)
    status: Optional[TaskStatus] = Field(None) 

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: TaskStatus
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True

class TaskListResponse(BaseModel):
    total: int
    skip: int
    limit: int
    items: list[TaskResponse]