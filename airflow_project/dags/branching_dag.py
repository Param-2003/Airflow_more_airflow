from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime

def decide_path():
    from random import choice
    path = choice(["process", "skip"])
    print(f"Branching to: {path}")
    return path

def process_data():
    print("✅ Processing data!")

def skip_data():
    print("❌ Skipping processing!")

with DAG(
    dag_id="branching_example",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["branching"]
) as dag:

    start = DummyOperator(task_id="start")

    branch = BranchPythonOperator(
        task_id="branch_logic",
        python_callable=decide_path
    )

    process = PythonOperator(
        task_id="process",
        python_callable=process_data
    )

    skip = PythonOperator(
        task_id="skip",
        python_callable=skip_data
    )

    end = DummyOperator(task_id="end", trigger_rule="none_failed_min_one_success")

    start >> branch >> [process, skip] >> end
