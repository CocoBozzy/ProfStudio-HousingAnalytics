from airflow import DAG
# We need to import the operators used in the tasks
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

import os
import pandas as pd

dag_path = os.getcwd

def transform_data():
    SydHousePrice = pd.read_csv(f"{dag_path}/raw_data/SydneyHousingPrice.csv", low_memory=False)

    # make date format consistent
    data.Date = pd.to_datetime(data.Date, infer_datetime_format=True)

    # load processed data
    data.to_csv(f"{dag_path}/processed_data/processed_data.csv", index=False)


# initializing the default arguments that we'll pass to our DAG
default_args = {
    'owner': 'airflow',
    'start_date': days_ago(5)
}

ingestion_dag = DAG(
    'SydneyHousePrice_ingestion',
    default_args=default_args,
    description='Aggregates housing price records for analysis',
    schedule_interval=timedelta(hours=1),
    catchup=False
)


task_1 = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=ingestion_dag,
)

task_2 = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=ingestion_dag,
)

task_1 >> task_2



