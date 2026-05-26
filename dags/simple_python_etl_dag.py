from __future__ import annotations

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator


def extract_data():
    """Simple extract task."""
    print("Step 1: Extracting data...")


def transform_data():
    """Simple transform task."""
    print("Step 2: Transforming data...")


def load_data():
    """Simple load task."""
    print("Step 3: Loading data...")


default_args = {
    "owner": "matrika",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


with DAG(
    dag_id="simple_python_etl_dag",
    description="A simple Python ETL DAG for Airflow",
    default_args=default_args,
    start_date=datetime(2026, 5, 26),
    schedule="@daily",
    catchup=False,
    tags=["simple", "python", "etl"],
) as dag:

    start = EmptyOperator(
        task_id="start"
    )

    extract = PythonOperator(
        task_id="extract_data",
        python_callable=extract_data,
    )

    transform = PythonOperator(
        task_id="transform_data",
        python_callable=transform_data,
    )

    load = PythonOperator(
        task_id="load_data",
        python_callable=load_data,
    )

    end = EmptyOperator(
        task_id="end"
    )

    start >> extract >> transform >> load >> end
