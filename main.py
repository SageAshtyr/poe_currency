import sys
import requests
import pandas as pd
import json


def get_data():
    url = "https://poe.ninja/api/data/currencyoverview?league=Kalandra&type=Currency"
    response = requests.get(url)
    if response.status_code != 200:
        print("Request to Poe.Ninja failed, most likely invalid league provided")
        sys.exit(1)
    return json.loads(response.text)["lines"]


def get_cor_pandas(lines: dict):
    pds = pd.DataFrame.from_dict(lines)[['currencyTypeName', 'chaosEquivalent']]
    return pds


def save_pandas(pds):
    pds.to_csv('poe_currency.csv', index=True)


save_pandas(get_cor_pandas(get_data()))
# print(get_corr_pandas(get_data()))