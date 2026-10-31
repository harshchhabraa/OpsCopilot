# OpsCopilot

AI-powered IT Operations and Incident Management Platform.

OpsCopilot combines machine learning, retrieval-augmented generation (RAG), and AI-assisted investigation to help IT operations teams manage incidents more efficiently.

## Planned Features

- Intelligent incident classification and routing
- Historical incident retrieval using vector search
- AI-powered incident investigation and summarization
- Knowledge base management
- Change risk prediction and explainability
- Ticket volume forecasting
- Human-in-the-loop AI approval workflows
- Workspace management and role-based access control
- Auditable operations

## Technology Stack

**Backend:** Python, FastAPI, SQLAlchemy, Alembic

**Infrastructure:** PostgreSQL, pgvector, Redis, Docker

**AI & Machine Learning:** Ollama, scikit-learn, LightGBM, SHAP

**Frontend:** React, TypeScript, Vite, Tailwind CSS

## Getting Started

### Prerequisites
- Python 3.12+
- Docker Desktop
- Node.js
- Ollama

### Start infrastructure

```bash
docker compose up -d
```

### Setup backend

```bash
cd backend
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

### Run the API

```bash
python -m uvicorn app.main:app --reload --port 8080
```

API documentation: http://127.0.0.1:8080/docs

## Project Status

Under active development.
