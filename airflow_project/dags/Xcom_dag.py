from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def push_function(**kwargs):
    message = "Hello from Task A!"
    kwargs['ti'].xcom_push(key='message_key', value=message)

def pull_function(**kwargs):
    ti = kwargs['ti']
    pulled_message = ti.xcom_pull(key='message_key', task_ids='push_task')
    print(f"Task B received: {pulled_message}")

with DAG(
    dag_id="xcom_example",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["xcom"]
) as dag:

    push_task = PythonOperator(
        task_id='push_task',
        python_callable=push_function,
        provide_context=True
    )

    pull_task = PythonOperator(
        task_id='pull_task',
        python_callable=pull_function,
        provide_context=True
    )

    push_task >> pull_task
