from datetime import datetime

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from api_test_dag.scripts.fetch_api_data import main_function


DAG = DAG(
    dag_id='api_test_dag',
    schedule_interval='@daily',
    start_date=datetime(2020, 1, 1),
    catchup=False,
)

fetch_task = PythonOperator(
    task_id='fetch_task',
    python_callable=main_function,
    dag=DAG,
)
