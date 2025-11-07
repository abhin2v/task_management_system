import pytest
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from app.database import engine, Base
from app.models.task import Task
from app.repositories.task import TaskRepository
from app.schemas.task import TaskCreate
from app.constants.enums import TaskStatus
from main import app

client = TestClient(app)

@pytest.fixture(autouse=True)
def cleanup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def test_create_task_repository():
    TestSession = sessionmaker(bind=engine)
    db = TestSession()
    
    repo = TaskRepository(db)
    task_data = TaskCreate(title="Learn FastAPI", description="Complete FastAPI tutorial", status=TaskStatus.PENDING)
    created_task = repo.create(task_data)
    
    assert created_task.id is not None
    assert created_task.title == "Learn FastAPI"
    assert created_task.status == TaskStatus.PENDING
    db.close()


def test_create_task_api_endpoint():
    task_data = {
        "title": "Buy groceries",
        "description": "Milk, eggs, bread",
        "status": "pending"
    }
    response = client.post("/tasks/", json=task_data)
    
    assert response.status_code == 201
    assert response.json()["title"] == "Buy groceries"
    assert response.json()["status"] == "pending"
    assert response.json()["id"] is not None