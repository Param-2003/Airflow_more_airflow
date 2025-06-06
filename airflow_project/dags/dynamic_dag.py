from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

cities = ["delhi", "paris", "newyork"]

with DAG(
    dag_id="dynamic_city_processing",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["dynamic"]
) as dag:
    for city in cities:
        BashOperator(
            task_id=f"process_{city}",
            bash_command=f"echo 'Processing city: {city}'"
        )
