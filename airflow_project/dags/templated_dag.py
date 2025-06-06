from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="templated_bash_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["template"]
) as dag:

    templated = BashOperator(
        task_id='templated_task',
        bash_command='echo "Running for date: {{ ds }}"'
    )
