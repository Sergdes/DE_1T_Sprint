from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import psycopg2


def save_function(article_list, name_outfile, w_or_a):
    with open(name_outfile, w_or_a,  encoding = 'UTF-8') as outfile:
        json.dump(article_list, outfile, ensure_ascii=False)

def hackernews_rss(source_link,name_source, name_outfile, w_or_a, **kwargs):
    try:
        r = requests.get(source_link)
        soup = BeautifulSoup(r.content, features='xml')
        articles = soup.findAll('item')
        article_list = []
        for a in articles:
            category = a.find('category').text
            source = name_source
            published = a.find('pubDate').text
            article = {
                'category': category,
                'source': source,
                'published': published
                }
            article_list.append(article)
        save_function(article_list,name_outfile, w_or_a)
    except Exception as e:
        print('Scraping failed. See exception:')
        print(e)

def create_table(conn, cursor):
    # Создание таблицы в базе данных при её отсутствии
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mytable (
            id SERIAL PRIMARY KEY,
            category VARCHAR(255),
            source VARCHAR(255),
            published TIMESTAMP
        )
    """)
    # Создание уникального или исключающего ограничения на нужных столбцах таблицы
    cursor.execute("""
        CREATE UNIQUE INDEX IF NOT EXISTS mytable_unique_idx
        ON mytable (published)
    """)
    conn.commit()

def populate_table(conn, cursor, data):
    # Заполнить таблицу указанными данными
    for row in data:
        cursor.execute("""
            INSERT INTO mytable (category, source, published)
            VALUES (%s, %s, %s)
            ON CONFLICT (published) DO NOTHING
        """, (row['category'], row['source'], row['published']))
    conn.commit()

def t4_to_postgres(outfile):
    ##Данные для подключения к БД.
    conn = psycopg2.connect(
        database='X_db', 
        user='XXX', 
        password='XXXXX',
        host='111.111.224.166',
        port='XXX'
    )
    cursor = conn.cursor()

 

    # Example data
    with open(outfile , 'r', encoding='UTF-8') as outfile:
        data = json.load(outfile)
    # Create and populate the table
    print(data)
    create_table(conn, cursor)
    populate_table(conn, cursor, data)

    # Clean up
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
    'DSS_dag_V5_14',
    default_args=default_args,
    description='',
    schedule_interval=timedelta(hours=24),
)

t1 = PythonOperator(
    task_id='hackernews_task_1',
    python_callable=hackernews_rss,
    op_args=('https://lenta.ru/rss/', 'lenta', 'outfile_1.json', 'w'),
    dag=dag,
)

t2 = PythonOperator(
    task_id='hackernews_task_2',
    python_callable=hackernews_rss,
    op_args=('https://www.vedomosti.ru/rss/news', 'vedomosti', 'outfile_2.json', 'w'),
    dag=dag,
)

t3 = PythonOperator(
    task_id='hackernews_task_3',
    python_callable=hackernews_rss,
    op_args=('https://tass.ru/rss/v2.xml', 'tass', 'outfile_3.json', 'w'),
    dag=dag,
)

to_sql_1 = PythonOperator(
    task_id='t4_to_postgres_1',
    python_callable=t4_to_postgres,
    op_args=('outfile_1.json',),
    dag=dag,
)

to_sql_2 = PythonOperator(
    task_id='t4_to_postgres_2',
    python_callable=t4_to_postgres,
    op_args=('outfile_2.json',),
    dag=dag,
)
to_sql_3 = PythonOperator(
    task_id='t4_to_postgres_3',
    python_callable=t4_to_postgres,
    op_args=('outfile_3.json',),
    dag=dag,
)


t1 >> to_sql_1 >> t2 >> to_sql_2 >> t3 >> to_sql_3  