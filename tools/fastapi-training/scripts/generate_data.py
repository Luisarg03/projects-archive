import os
import glob
import pandas as pd
import psycopg2
from time import sleep
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import INTEGER, VARCHAR, FLOAT, BOOLEAN


DBNAME = os.environ['DATABASE_NAME']
USER = os.environ['DATABASE_USER']
PASSWORD = os.environ['DATABASE_PASSWORD']
HOST = os.environ['DATABASE_HOST']


def connect_to_database(retries=4, delay=15):
    while retries:
        try:
            return psycopg2.connect(
                dbname=os.environ['DATABASE_NAME'],
                user=os.environ['DATABASE_USER'],
                password=os.environ['DATABASE_PASSWORD'],
                host=os.environ['DATABASE_HOST']
            )
        except psycopg2.OperationalError as e:
            retries -= 1
            print(e)
            print("Error al conectar a la base de datos, reintentando...")
            sleep(delay)

    raise Exception("No se pudo conectar a la base de datos")


conn = connect_to_database(retries=5, delay=10)


csv_files = glob.glob('./data/*.csv')
engine = create_engine(f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:5432/{DBNAME}')

for file in csv_files:
    table_name = file.replace('\\', '/')
    table_name = table_name.split('/')[-1].split('.')[0]
    chunksize = 1000000
    iterator = pd.read_csv(filepath_or_buffer=file, sep=',', header=0, chunksize=chunksize)

    for i, chunk in enumerate(iterator):
        chunk['row_id'] = range(i * chunksize, i * chunksize + len(chunk))

        dtype_dict = {
            col: VARCHAR() if dtype == 'object'
            else FLOAT() if dtype == 'float64'
            else INTEGER() if dtype == 'int64'
            else BOOLEAN() if dtype == 'bool'
            else VARCHAR()
            for col, dtype in chunk.dtypes.items()
        }

        if_exists_method = 'replace' if i == 0 else 'append'
        chunk.to_sql(table_name, con=engine, if_exists=if_exists_method, index=False, dtype=dtype_dict)

    print(f"Data INSERT on {table_name}")

print("Generate data finished")
