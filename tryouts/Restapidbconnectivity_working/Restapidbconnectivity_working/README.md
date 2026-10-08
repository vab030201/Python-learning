# TFLInsurance REST API

## 1. Create database
Run in MySQL Workbench:

```sql
CREATE DATABASE IF NOT EXISTS tflinsurance;
```

## 2. Set MySQL password
Set environment variables before running:

Windows CMD:

```cmd
set DB_USER=root
set DB_PASSWORD=YOUR_MYSQL_PASSWORD
set DB_HOST=localhost
set DB_PORT=3306
set DB_NAME=tflinsurance
```

PowerShell:

```powershell
$env:DB_USER="root"
$env:DB_PASSWORD="YOUR_MYSQL_PASSWORD"
$env:DB_HOST="localhost"
$env:DB_PORT="3306"
$env:DB_NAME="tflinsurance"
```

## 3. Install

```bash
python -m pip install -r requirements.txt
```

## 4. Run

```bash
uvicorn app.main:app --reload
```

Open Swagger:

http://127.0.0.1:8000/docs

## 5. Sample data
On the first startup, five sample policies are inserted automatically if the table is empty.

Endpoints:

- GET /api/policies/
- GET /api/policies/{policy_id}
- POST /api/policies/
- PUT /api/policies/{policy_id}
- DELETE /api/policies/{policy_id}
