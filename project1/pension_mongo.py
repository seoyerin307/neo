import pandas as pd
from pymongo import MongoClient
import os.path
import json

df = pd.read_csv('pension_prediction_2100syr.csv', encoding='utf-8')

print(df.head())  # year, amount_per_person

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath("./")))
secret_file = os.path.join(BASE_DIR, '../secret.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg

HOSTNAME = get_secret("ATLAS_Hostname")
USERNAME = get_secret("ATLAS_Username")
PASSWORD = get_secret("ATLAS_Password")

client = MongoClient(f"mongodb+srv://{USERNAME}:{PASSWORD}@{HOSTNAME}")
db = client["pension"]  
col = db["pension_predictions"]  


data_dict = df.to_dict("records")
col.insert_many(data_dict)
