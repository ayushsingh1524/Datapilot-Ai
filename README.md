# DataPilot AI

> **Intelligent Data Engineering & Analytics Platform**

DataPilot AI is an end-to-end data engineering and AI analytics platform that turns raw order data into reliable analytics and natural-language insights.

The platform combines **ETL, data quality validation, PostgreSQL, pgvector, RAG, Gemini AI, safe SQL generation, anomaly detection, FastAPI, React, and Docker** in one portfolio-ready project.

---

## 🚀 What It Does

```text
Raw CSV
  ↓
Ingestion
  ↓
Validation + Profiling
  ↓
Transformation
  ↓
PostgreSQL + pgvector
  ↓
┌───────────────────────┬────────────────────────┐
│                       │                        │
Analytics          Anomaly Detection        Schema RAG
│                       │                        │
└───────────────────────┴───────────┬────────────┘
                                    ↓
                               Gemini AI
                                    ↓
                         Natural Language → SQL
                                    ↓
                              SQL Guardrails
                                    ↓
                         Read-only PostgreSQL
                                    ↓
                               FastAPI
                                    ↓
                            React Dashboard
```

---

## ✨ Features

### Data Engineering
- CSV ingestion using Pandas
- Data quality validation
- Data profiling
- Data transformation and cleaning
- Calculated `total_amount` metric
- PostgreSQL data warehouse-style storage
- Incremental loading that avoids duplicate order IDs

### Analytics
- Total revenue
- Total orders
- Average order value
- Revenue by product
- Revenue by region
- Daily revenue
- SQL-based analytics queries

### AI Analytics
- Google Gemini integration
- Natural-language analytics
- NL → SQL generation
- Schema-aware RAG
- pgvector similarity search
- Conversational analytics with session history
- AI-generated result explanations

### Anomaly Detection
- IQR-based statistical anomaly detection
- Detects unusual order values and quantities
- AI-generated anomaly explanations
- Statistical fallback explanation if AI explanation fails

### Security / Reliability
- Only `SELECT` and `WITH` SQL queries are allowed
- Destructive SQL keywords are blocked
- Multiple SQL statements are rejected
- Read-only database transactions
- PostgreSQL statement timeout
- Result-row limit
- Input validation for chat requests

### Application
- FastAPI REST backend
- Interactive React dashboard
- Recharts visualizations
- Dockerized services
- Pytest test suite

---

## 🛠️ Tech Stack

| Area | Technologies |
|---|---|
| Language | Python 3.13 |
| Data Engineering | Pandas |
| Database | PostgreSQL 16 |
| Vector Search | pgvector |
| ORM / DB Access | SQLAlchemy |
| AI | Google Gemini |
| Embeddings | Sentence Transformers |
| RAG | pgvector + schema retrieval |
| API | FastAPI, Pydantic |
| Frontend | React, Vite, Recharts |
| Server | Uvicorn, Nginx |
| Testing | Pytest |
| Containers | Docker, Docker Compose |
| Package Manager | uv |

---

## 📁 Project Structure

```text
datapilot-ai/
│
├── api/
│   ├── main.py
│   └── routes/
│       ├── analytics.py
│       ├── anomalies.py
│       └── chat.py
│
├── data/
│   ├── raw/
│   │   └── orders.csv
│   └── processed/
│
├── frontend/
│   ├── src/
│   ├── Dockerfile
│   └── package.json
│
├── sql/
│   ├── analytics.sql
│   └── schema.sql
│
├── src/
│   ├── ai/
│   │   ├── anomaly_explainer.py
│   │   ├── embeddings.py
│   │   ├── explainer.py
│   │   ├── index_schema.py
│   │   ├── retriever.py
│   │   ├── schema_documents.py
│   │   ├── schema_loader.py
│   │   ├── sql_generator.py
│   │   ├── sql_validator.py
│   │   └── vector_store.py
│   │
│   ├── analytics/
│   │   └── anomaly_detection.py
│   │
│   ├── database/
│   │   ├── connection.py
│   │   ├── load.py
│   │   └── queries.py
│   │
│   ├── ingestion/
│   │   └── csv_loader.py
│   │
│   ├── transformation/
│   │   └── transform.py
│   │
│   └── validation/
│       ├── profiler.py
│       └── quality_checks.py
│
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── main.py
├── pyproject.toml
├── uv.lock
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd datapilot-ai
```

### 2. Create the environment

```bash
uv sync
```

### 3. Configure environment variables

Create `.env` from `.env.example`:

```env
DB_HOST=127.0.0.1
DB_PORT=5436
DB_NAME=datapilot
DB_USER=postgres
DB_PASSWORD=postgres

GEMINI_API_KEY=your_gemini_api_key_here
```

**Never commit your real `.env` file or API key.**

---

## 🐘 PostgreSQL + pgvector

The project uses the `pgvector/pgvector:pg16` Docker image.

Start PostgreSQL:

```bash
docker compose up -d postgres
```

The database is exposed locally on:

```text
localhost:5436
```

The application database is:

```text
datapilot
```

Initialize the schema:

```bash
docker exec -i datapilot-postgres psql   -U postgres   -d datapilot < sql/schema.sql
```

The schema contains:

- `orders`
- `schema_embeddings`

The `vector` extension is enabled for semantic schema retrieval.

---

## 🔄 Run the ETL Pipeline

Run:

```bash
uv run python main.py
```

The pipeline:

1. Reads `data/raw/orders.csv`
2. Validates required columns
3. Checks null and duplicate values
4. Profiles the dataset
5. Cleans and transforms fields
6. Calculates `total_amount`
7. Loads new records into PostgreSQL

Example transformation:

```text
total_amount = price × quantity
```

The loader checks existing `order_id` values so rerunning the pipeline does not insert duplicate orders.

---

## 📊 Analytics

SQL analytics are stored in:

```text
sql/analytics.sql
```

Available analytics include:

```text
Total revenue
Total orders
Average order value
Revenue by product
Revenue by region
Daily revenue
```

For the included 20-order sample dataset, the current ETL results are:

| Metric | Value |
|---|---:|
| Total Orders | 20 |
| Total Revenue | ₹440,200 |
| Average Order Value | ₹22,010 |

---

## 🤖 AI + RAG Pipeline

DataPilot AI uses a schema-aware RAG pipeline to help Gemini generate SQL against the actual database structure.

```text
User Question
      ↓
Generate Query Embedding
      ↓
pgvector Similarity Search
      ↓
Retrieve Relevant Schema / Business Rules
      ↓
Gemini SQL Generation
      ↓
SQL Validator
      ↓
Read-only PostgreSQL Query
      ↓
Query Results
      ↓
Gemini Explanation
      ↓
Natural-language Answer
```

### Why RAG?

Instead of sending the entire database description every time, the system retrieves the most relevant schema/business-rule context for the user's question.

The schema embeddings are stored in PostgreSQL using pgvector.

The embedding model used by the project is:

```text
all-MiniLM-L6-v2
```

with:

```text
384-dimensional embeddings
```

---

## 💬 Natural-Language Analytics

Start the API and ask questions such as:

```text
Which product generated the highest revenue?

What was the total revenue from laptops?

Which region generated the most revenue?

Show me the daily revenue.

Which orders were detected as anomalies?
```

The system converts the natural-language question into SQL, validates it, executes it safely, and explains the result.

Example generated query:

```sql
SELECT SUM(total_amount) AS total_revenue
FROM orders
WHERE product = 'Laptop'
```

---

## 🔐 SQL Safety

AI-generated SQL is **never executed directly**.

The validation layer:

- Allows only `SELECT` and `WITH`
- Blocks `DROP`
- Blocks `DELETE`
- Blocks `UPDATE`
- Blocks `INSERT`
- Blocks `ALTER`
- Blocks `TRUNCATE`
- Blocks `CREATE`
- Blocks `GRANT`
- Blocks `REVOKE`
- Rejects multiple SQL statements
- Executes queries using a read-only transaction
- Applies a PostgreSQL statement timeout
- Limits returned rows

This provides an important guardrail between an LLM and the database.

---

## 🚨 Anomaly Detection

The project uses the **Interquartile Range (IQR)** method to detect unusual orders.

The anomaly pipeline checks:

```text
total_amount
quantity
```

For the included sample dataset, the statistical detector currently identifies **3 anomalies**.

The API can then use Gemini to generate a short human-readable explanation.

If the AI explanation is unavailable, the API falls back to a statistical explanation.

---

## 🌐 FastAPI

Start the API locally:

```bash
uv run uvicorn api.main:app --reload --port 8000
```

API:

```text
http://localhost:8000
```

Swagger documentation:

```text
http://localhost:8000/docs
```

### Endpoints

#### Analytics

```http
GET /analytics/summary
GET /analytics/products
GET /analytics/regions
GET /analytics/daily
```

#### Anomaly Detection

```http
GET /anomalies
```

#### AI Chat

```http
POST /chat
```

The chat API supports conversational context using a session ID.

---

## 🎨 React Dashboard

The frontend provides:

- Revenue overview
- Order count
- Average order value
- Product revenue chart
- Regional revenue chart
- Daily revenue chart
- Anomaly detection panel
- AI chat interface
- System status indicators

Run the frontend locally:

```bash
cd frontend
npm install
npm run dev
```

The development dashboard runs on:

```text
http://localhost:5174
```

---

## 🐳 Run Everything with Docker

Build the services:

```bash
docker compose build
```

Start everything:

```bash
docker compose up -d
```

Check containers:

```bash
docker compose ps
```

Services:

| Service | URL / Port |
|---|---|
| React Dashboard | `http://localhost:5174` |
| FastAPI | `http://localhost:8000` |
| Swagger Docs | `http://localhost:8000/docs` |
| PostgreSQL | `localhost:5436` |

Stop services:

```bash
docker compose down
```

---

## 🧪 Testing

Run the complete test suite:

```bash
uv run pytest
```

The test suite covers:

- Data validation
- Data transformation
- Anomaly detection
- SQL validation
- Analytics API
- Anomaly API
- Chat API input validation

Current project test status:

```text
20 passed
1 warning
```

The warning is a non-blocking dependency deprecation warning.

---

## 📌 Engineering Concepts Demonstrated

This project demonstrates practical experience with:

- ETL pipeline design
- Data ingestion
- Data validation
- Data profiling
- Data transformation
- Incremental database loading
- Relational database design
- SQL analytics
- PostgreSQL
- Vector databases
- Embeddings
- Retrieval-Augmented Generation
- LLM integration
- Natural-language-to-SQL
- SQL guardrails
- Read-only query execution
- Statistical anomaly detection
- REST API development
- React dashboards
- Data visualization
- Docker containerization
- Automated testing

---

## 🔮 Future Enhancements

Planned improvements include:

- Apache Airflow workflow orchestration
- Additional CSV/JSON/API data sources
- More advanced anomaly detection
- Persistent conversation history
- Authentication and authorization
- Cloud deployment
- Monitoring and observability
- Production-grade logging
- CI/CD pipeline

---

## 🎯 Resume Project Summary

**DataPilot AI — Intelligent Data Engineering & Analytics Platform**

Built an end-to-end data engineering and AI analytics platform using **Python, Pandas, PostgreSQL, pgvector, FastAPI, React, Docker, and Gemini**, implementing ETL, data quality validation, anomaly detection, schema-aware RAG, natural-language-to-SQL, SQL guardrails, conversational analytics, and interactive dashboards.

---

## 📄 License

This project is intended for learning, portfolio, and demonstration purposes.
