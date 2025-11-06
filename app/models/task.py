from sqlalchemy import Column, Integer, String, Text, DateTime, Enum as SQLAlchemyEnum
from sqlalchemy.sql import func
from app.database import Base
from app.constants.enums import TaskStatus

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=True, nullable=False, index=True)
    description = Column(Text)
    status = Column(
        SQLAlchemyEnum(TaskStatus),
        default=TaskStatus.PENDING,
        nullable=False
    )
    created_at = Column(DateTime(timezone=True), server_default=func.current_date())
    updated_at = Column(DateTime, onupdate=func.current_date())

    def __repr__(self):
        return f"<Task(Id={self.id}, Title={self.title}, Status={self.status})>"