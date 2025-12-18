from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def print_hello():
  print("Hello from Airflow DAG!")


with DAG(
    dag_id="hello_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    description="Simple test DAG that prints Hello",
) as dag:
    hello_task = PythonOperator(
        task_id="hello_task",
        python_callable=print_hello,
    )