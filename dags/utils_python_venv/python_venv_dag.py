from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonVirtualenvOperator
from utils_python_venv.scripts.code import print_venv

dag = DAG(
    dag_id='python_venv_dag',
    schedule_interval='0 0 * * *',
    start_date=datetime(2020, 1, 1),
    catchup=False
)

venv_task = PythonVirtualenvOperator(
    task_id='venv_task',
    python_callable=print_venv,
    requirements=['numpy==1.18.1'],
    system_site_packages=False,
    dag=dag
)

