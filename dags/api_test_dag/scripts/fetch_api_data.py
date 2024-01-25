from typing import Optional, List
import psycopg2
import pprint

import requests

BASE_URL = 'http://universities.hipolabs.com/search?country=United+States'
DB_CONN = 'postgresql+psycopg2://airflow:airflow@postgres/airflow'


def fetch_api_data(url: Optional[str] = None) -> List[dict]:
    if url is None:
        url = BASE_URL

    response = requests.get(url)
    return response.json()


def process_api_data(data: List[dict]) -> None:
    for item in data:
        print(item['name'])
        print(item['alpha_two_code'])
        print(item['country'])
        print(item['domains'])
        print(item['state-province'])
        print(item['web_pages'])


def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname='airflow',
            user='airflow',
            host='localhost',
            port='5433',
            password='airflow'
        )
        cur = conn.cursor()

        if conn is not None:
            print("Connected to the database")
            return cur  # You might want to return cursor, to use it outside this function

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)
        return None  # Returning None if something went wrong


def insert_data(cur, data):
    try:
        cur.execute("INSERT INTO universities "
                    "(name, alpha_two_code, country, domains, state_province, web_pages)"
                    " VALUES (%s, %s, %s, %s, %s, %s)",
                    (data['name'], data['alpha_two_code'], data['country'], data['domains'],
                     data['state-province'], data['web_pages']))
        print("Inserted data")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while inserting data to PostgreSQL", error)


def main_function():
    data = fetch_api_data()
    process_api_data(data)
    connect_to_db()
    for item in data:
        insert_data(connect_to_db(), data)

# main_function()
