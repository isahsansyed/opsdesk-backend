# OpsDesk Backend

Real-time support & incident management platform backend.

## Stack
- FastAPI (Python 3.12+)
- PostgreSQL + Async SQLAlchemy 2.0
- Redis (cache + Pub/Sub)
- Alembic (migrations)
- Docker & Docker Compose

## Status
Day 3 — FastAPI app bootstrapped.

## Docs
See [`docs/`](./docs) for architecture, database design, RBAC, ticket lifecycle, and API surface.

## Running locally
```bash
python -m venv .venv
source .venv/Scripts/activate    # Git Bash on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open http://127.0.0.1:8000/docs