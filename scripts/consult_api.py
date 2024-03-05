#Script para consultar api de MELI

import requests
import json
import datetime

DATE = str(datetime.date.today()).replace('-', '')

def get_most_relevant_items_for_category(category):
    url = f"https://api.mercadolibre.com/sites/MLA/search?category={category}#json"
    response = requests.get(url).text
    response = json.loads(response)
    data = response['results']

    with open('/Users/belen/Desktop/airflow-docker/file.tsv', 'w') as file:
        for item in data:
            _id = getKeyFromItem(item, 'id')
            tittle = getKeyFromItem(item, 'tittle')
            price = getKeyFromItem(item, 'price')
            sold_quantity = getKeyFromItem(item, 'sold_quantity')
            thumbnail = getKeyFromItem(item, 'thumbnail')

            file.write(f"{_id} {tittle} {price} {sold_quantity} {thumbnail} {DATE}\n")


def getKeyFromItem(item, key):
    return str(item[key]).replace(' ', '').strip() if item.get(key) else "null"

def main():
    CATEGORY = "MLA1577"
    get_most_relevant_items_for_category(CATEGORY)


main()