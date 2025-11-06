from fastapi import FastAPI
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

@app.get("/")
def read_root():
    return {"message": "root request"}

@app.get("/health", status_code=200)
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app",host="0.0.0.0", reload=True, port=8000)