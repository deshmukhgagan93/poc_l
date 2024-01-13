from typing import Optional, List
import pprint
import psycopg2

import requests

BASE_URL = 'http://universities.hipolabs.com/search?country=United+States'


def fetch_api_data(url: Optional[str] = None) -> List[dict]:
    if url is None:
        url = BASE_URL

    response = requests.get(url)
    return response.json()


def process_api_data(data: List[dict]) -> None:
    for item in data:
        print(item['name'])
        # print(item['alpha_two_code'])
        # print(item['country'])
        # print(item['domains'])
        # print(item['state-province'])
        # print(item['web_pages'])


def main_function():
    data = fetch_api_data()
    process_api_data(data)



