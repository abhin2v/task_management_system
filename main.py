from fastapi import FastAPI, status
from app.database import Base, engine
from app.models.task import Task

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

@app.get("/")
def read_root():
    return {"message": "root request"}

@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app",host="0.0.0.0", reload=True, port=8000)