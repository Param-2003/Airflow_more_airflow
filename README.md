# 🛠️ Apache Airflow Projects Portfolio

This repository showcases my hands-on learning and practice with Apache Airflow, focusing on real-world data engineering use cases. Each project is containerized using Docker and scheduled with Airflow DAGs.

---

## 🧰 Tech Stack
- Apache Airflow
- Python
- Docker
- Pandas / PySpark (for ETL)
- Jinja templating
- Kafka (for advanced pipeline)
- AWS S3 (optional, simulated locally)

---

## 📂 Project Structure

| Folder | Description |
|--------|-------------|
| `dags/` | All DAG definitions — XCom, templating, branching, ETL jobs |
| `etl_scripts/` | ETL logic (data cleaning, transformation) |
| `data/` | Sample datasets for input/output |
| `notebooks/` | Jupyter notebooks to test scripts |
| `docker-compose.yaml` | Spins up Airflow locally using Docker |

---

## 📌 DAGs Included

- `xcom_example.py` – Sharing data between tasks using XCom
- `branching_example.py` – Conditional task branching
- `templating_example.py` – Jinja templating in BashOperator
- `micro_batch_etl.py` – Simulated micro-batching with data polling
- `streaming_trigger_dag.py` – Orchestrating a streaming-like job

---

## 🚀 Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/airflow-projects-portfolio.git
   cd airflow-projects-portfolio
