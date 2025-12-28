# Data Ingestion Pipeline with MinIO and Python

Local Data Lake environment using Docker containers for automated data ingestion with synthetic records.

## Technologies
- **Python 3.12+**: Automation and ingestion scripting.
- **Docker & Docker Compose**: Service orchestration.
- **MinIO**: S3-compatible Object Storage (Data Lake).
- **Pandas & Faker**: Data manipulation and Mock Data generation.
- **Boto3**: AWS SDK for Python to interact with MinIO.

## Architecture
[Python Script] --(Generates Data)--> [Pandas DataFrame] --(Streaming Upload)--> [MinIO Bucket 'raw-data']

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Python 3.12+

### Setup

1. **Start MinIO:**
```bash
cd docker/minio
docker compose up -d
```

2. **Start Portainer (optional):**
```bash
cd docker/portainer
docker compose up -d
```

3. **Setup Python environment:**
```bash
cd scripts
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

4. **Run ingestion:**
```bash
python ingestion.py
```

## Access

- **MinIO Console**: http://localhost:9001 (minio/minio123)
- **MinIO API**: http://localhost:9000 (minio/minio123)
- **Portainer**: http://localhost:9003

## Data Schema

Generated CSV files contain: `name`, `city`, `email`, `amount` (10-1000), `date`
- 100 records per run
- Files: `generic_example_YYYY-MM-DD_HH-MM.csv`
- Stored in `raw-data` bucket

## Service Management

```bash
# View logs
docker compose logs -f

# Stop services
docker compose down

# Clean up (removes all data)
docker compose down -v
```
