from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor
from datetime import datetime

with DAG(
    dag_id="file_sensor_example",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["sensor"]
) as dag:

    wait_for_file = FileSensor(
        task_id="wait_for_file",
        filepath="/opt/airflow/dags/data/pears_production.csv",  # Put a dummy file here
        poke_interval=10,
        timeout=60,
        mode="poke"
    )

    process_file = BashOperator(
        task_id="process_file",
        bash_command="echo 'Processing file now...'"
    )

    wait_for_file >> process_file
