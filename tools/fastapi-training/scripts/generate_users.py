import json
import os
import hashlib
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

DIGEST = os.environ.get('DIGEST')
ROUNDS = int(os.environ.get('ROUNDS'))

DBNAME = os.environ['DATABASE_NAME']
USER = os.environ['DATABASE_USER']
PASSWORD = os.environ['DATABASE_PASSWORD']
HOST = os.environ['DATABASE_HOST']

table_name = "users_api"
engine = create_engine(f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:5432/{DBNAME}')

with open('data/users.json', 'r') as file:
    users = json.load(file)

# Encrypt passwords using SHA256
for user in users.items():
    password = user[1]['password']
    encrypted_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), DIGEST.encode('utf-8'), ROUNDS)
    user[1]['password'] = encrypted_password.hex()

df = pd.DataFrame(list(users.values()))
df["row_id"] = df.index
df.to_sql(table_name, con=engine, if_exists='replace', index=False)
