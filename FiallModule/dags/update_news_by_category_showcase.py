from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import psycopg2


 

def update_news_by_category_showcas():
    ##Данные для подключения к БД.
    conn = psycopg2.connect(
        database='X_db', 
        user='XXX', 
        password='XXXXX',
        host='111.111.224.166',
        port='XXX'
    )
    cursor = conn.cursor()

    # Создание таблицы в базе данных при её отсутствии
    cursor.execute("""
        DROP TABLE IF EXISTS news_by_category_showcase;
    """)
    # Создание таблицы витрины данных
    cursor.execute("""
       CREATE TABLE news_by_category_showcase AS
        SELECT
        ROW_NUMBER() OVER (ORDER BY category) AS category_id,
        category,
        COUNT(*) AS total_news_count_all_sources,
        COUNT(*) FILTER (WHERE source = 'lenta') AS news_count_lenta,
        COUNT(*) FILTER (WHERE source = 'vedomosti') AS news_count_vedomosti,
        COUNT(*) FILTER (WHERE source = 'tass') AS news_count_tass,
        COUNT(*) FILTER (WHERE published >= now() - interval '1 day') AS total_news_count_last_day,
        COUNT(*) FILTER (WHERE source = 'lenta' AND published >= now() - interval '1 day') AS news_count_lenta_last_day,
        COUNT(*) FILTER (WHERE source = 'vedomosti' AND published >= now() - interval '1 day') AS news_count_v_l_day,
        COUNT(*) FILTER (WHERE source = 'tass' AND published >= now() - interval '1 day') AS news_count_t_l_day
        FROM mytable
        GROUP BY category
        ORDER BY category;
    """)
    conn.commit()
    cursor.close()
    conn.close()  
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 2, 26),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'DSS_update_news_by_category_showcase_V3',
    default_args=default_args,
    description='',
    schedule_interval=timedelta(hours=24),
)

update_showcas = PythonOperator(
    task_id='update_news_by_category_showcas',
    python_callable=update_news_by_category_showcas,

    dag=dag,
)

update_showcas