from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from scripts.consult_api import get_most_relevant_items_for_category

with DAG(
    dag_id = 'first_dag', 
    start_date = datetime(2023,2,17)
): 
   
    task_2 = BashOperator (
        task_id = "first task",
        bash_command = "echo 'Hello world'"
    )

    task_3 = PythonOperator(
    task_id='extract_task',
    python_callable=get_most_relevant_items_for_category,
    op_kwargs={'category': 'MLA1577'},
    
    )

    task_4 = BashOperator (
        task_id = "last task",
        bash_command = "echo 'Bye world'"
    )

task_2 >> task_3

    ##https://api.mercadolibre.com/sites/MLA/search?category=MLA1577#json