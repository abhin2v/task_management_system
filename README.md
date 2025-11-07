# Task Manager API

A FastAPI application for managing tasks with SQLAlchemy ORM and SQLite database.

## Setup

### 1. Install Dependencies
```bash
python3 -m venv fastapi_env 
source fastapi_env/bin/activate
pip3 install -r requirement.txt
```

### 2. Run Application
```bash
python3 main.py
```

The API will be available at: `http://localhost:8000`

## Database

SQLite database `tasks.db` is automatically created on startup.

No manual migrations needed.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/tasks/` | Create task |
| GET | `/tasks/` | List tasks |
| GET | `/tasks/{id}` | Get single task |
| PUT | `/tasks/{id}` | Update task |
| DELETE | `/tasks/{id}` | Delete task |

## Running Tests

```bash
python3 -m pytest app/tests/test.py -v
```

## Project Structure

```
.
├── app
│   ├── constants
│   │   └── enums.py
│   ├── database.py
│   ├── models
│   │   └── task.py
│   ├── repositories
│   │   └── task.py
│   ├── routes
│   │   └── task.py
│   ├── schemas
│   │   └── task.py
│   └── tests
│       └── test.py
├── main.py
├── README.md
├── remove_pyc.py
├── requirement.txt
└── tasks.db

7 directories, 12 files

```

## Example Usage

**Create task:**
```bash
curl -X POST "http://localhost:8000/tasks/" \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn FastAPI", "status": "pending"}'
```

**List tasks:**
```bash
curl "http://localhost:8000/tasks/"
```

**Get single task:**
```bash
curl "http://localhost:8000/tasks/1"
```

**Update task:**
```bash
curl -X PUT "http://localhost:8000/tasks/1" \
  -H "Content-Type: application/json" \
  -d '{"status": "completed"}'
```

**Delete task:**
```bash
curl -X DELETE "http://localhost:8000/tasks/1"
```