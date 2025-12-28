# Data Ingestion Pipeline with MinIO and Python

This project demonstrates a local **Data Lake** environment using Docker containers. It focuses on Infrastructure as Code (IaC) principles and automated data ingestion using synthetic records.

## Technologies
- **Python 3.12+**: Automation and ingestion scripting.
- **Docker & Docker Compose**: Service orchestration.
- **MinIO**: S3-compatible Object Storage (Data Lake).
- **Pandas & Faker**: Data manipulation and Mock Data generation.
- **Boto3**: AWS SDK for Python to interact with MinIO.

## Architecture
[Python Script] --(Generates Data)--> [Pandas DataFrame] --(Streaming Upload)--> [MinIO Bucket 'raw-data']

## 🚀 Getting Started

### 1. Prerequisites
- Docker and Docker Compose installed.
- Python 3.12+ installed.

### 2. Spinning up Infrastructure
From the project root:
```bash
cd docker/minio
docker compose up -d
