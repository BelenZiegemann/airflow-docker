from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.postgres_operator import PostgresOperator
from datetime import datetime

with DAG(
    dag_id = 'first_dag', 
    start_date = datetime(2023,2,17)
): 
   
    task_2 = BashOperator (
        task_id = "saludando",
        bash_command = "echo 'Hola mundo'"
    )

    task_2

    ##https://api.mercadolibre.com/sites/MLA/search?category=MLA1577#json