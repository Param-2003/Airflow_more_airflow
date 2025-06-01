from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello_python():
    print("👋 Hello from PythonOperator!")

with DAG(
    dag_id="first_custom_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["tutorial"]
) as dag:

    t1 = BashOperator(
        task_id="bash_says_hi",
        bash_command="echo 'Hello from Bash!'"
    )

    t2 = PythonOperator(
        task_id="python_says_hi",
        python_callable=hello_python
    )

    t1 >> t2
