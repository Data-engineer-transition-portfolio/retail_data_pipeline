# 📦 Retail Data Pipeline

---

## Project Structure

```bash
retail_data_pipeline/
│
├── data/                  # Raw and processed data
├── src/
│   ├── extract.py         # Download & read CSV
│   ├── transform.py       # Cleaning & aggregation
│   ├── load.py            # Write to PostgreSQL
│   └── utils.py           # Helper functions
├── notebooks/             # EDA and testing notebooks
├── tests/                 # Unit tests
├── Dockerfile             # Docker container setup
├── requirements.txt       # Project dependencies
└── README.md              # Project overview
```

---

# 📄 requirements.txt

```txt
pandas
sqlalchemy
psycopg2-binary
requests
python-dotenv
loguru
```

_Optional additions for expansion:_
```txt
prefect    # For orchestration (optional)
airflow    # For production DAGs (optional)
pytest     # For testing
jupyterlab # If you want to run notebooks
```

---

# 🐳 Dockerfile

```Dockerfile
# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY src/ src/
COPY data/ data/
COPY tests/ tests/
COPY notebooks/ notebooks/

# Environment Variables (Optional if using .env)
ENV PYTHONUNBUFFERED=1

# Default command
CMD ["python", "src/extract.py"]
```

---

# 📚 README.md

## Retail Data Pipeline

### Project Overview
This project builds a **Retail Analytics Data Pipeline** to ingest, transform, and load retail sales data sourced from Kaggle into a PostgreSQL database. It prepares structured, clean datasets ready for analytics and dashboarding.

---

### Features
- Extract raw data from Kaggle datasets (local CSV)
- Clean and normalize retail sales data
- Aggregate data weekly and monthly
- Load cleaned data into a PostgreSQL database
- Dockerized for easy deployment
- Structured for future integration with orchestration tools like Airflow or Prefect

---

### Folder Structure

```bash
retail_data_pipeline/
│
├── data/                  # Raw and processed data
├── src/
│   ├── extract.py         # Download & read CSV
│   ├── transform.py       # Cleaning & aggregation
│   ├── load.py            # Write to PostgreSQL
│   └── utils.py           # Helper functions
├── notebooks/             # EDA and testing notebooks
├── tests/                 # Unit tests
├── Dockerfile             # Docker container setup
├── requirements.txt       # Project dependencies
└── README.md              # Project overview
```

---

### Setup Instructions

#### 1. Clone the repository
```bash
git clone <repo_url>
cd retail_data_pipeline
```

#### 2. Set up environment variables (optional)
Create a `.env` file if needed for database connections.
```env
POSTGRES_USER=your_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=your_db
POSTGRES_HOST=your_host
POSTGRES_PORT=5432
```

#### 3. Run Locally
Install dependencies:
```bash
pip install -r requirements.txt
```

Run scripts individually:
```bash
python src/extract.py
python src/transform.py
python src/load.py
```

#### 4. Run with Docker
```bash
docker build -t retail-data-pipeline .
docker run --env-file .env retail-data-pipeline
```

---

### Future Enhancements
- Add Airflow DAGs for full orchestration.
- Add incremental loading feature.
- Export a dashboard-ready API.
- Integrate with cloud storage (AWS S3, Azure Blob).

---

### Author
Built with ❤️ by Godswill David.
