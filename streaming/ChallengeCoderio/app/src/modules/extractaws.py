#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import re
import boto3
import pandas as pd
from sqlalchemy import types


def ping_aws(client, bucket):
    '''
    Test connection with AWS

    Parameters
    ----------
    client : boto.client obj
        client obj boto3
    bucket: str
        Name bucket s3
    
    Returns
    ---------
    bool
    '''
    while True:
        status = client.list_objects(Bucket=bucket)['ResponseMetadata']['HTTPStatusCode']
        if status == 200:
            break
        else:
            time.seep(10)
            pass
    return True


def extract(engine, config_aws, schema, bucket, file_source):    
    '''
    Extract files of S3

    Parameters
    ----------
    engine : sqlalchemy engine
        engine db
    config_aws: dict
        dict config credentials aws
    schema : str
        schema db
    bucket: str
        Name bucket s3
    file_source: str
        name or extract of path in aws s3
    
    Returns
    ---------
    rows_insert: int
        number of row insert in db
    '''

    client = boto3.client(**config_aws)
    rows_insert = []

    for key in client.list_objects(Bucket=bucket)['Contents']:
        file_name = key['Key']
        obj = client.get_object(Bucket=bucket, Key=key['Key'])
        if file_source in file_name:
            for df in pd.read_csv(obj['Body'], chunksize=20000, low_memory=False):
                
                df = df.astype(str)
                dtype = {c:types.VARCHAR(350)
                        for c in df.columns[df.dtypes == 'object'].tolist()}
                
                for currency in df['currency'].unique():
                    if 'init' in file_source:
                        df.loc[df['currency'] == currency].to_sql(name='RAW_DATA_INIT_'+currency, con=engine, schema=schema, if_exists='append', index=False, dtype=dtype)
                    elif 'increment' in file_source:
                        df.loc[df['currency'] == currency].to_sql(name='RAW_DATA_'+currency, con=engine, schema=schema, if_exists='append', index=False, dtype=dtype)
                    else:
                        pass

                    rows_insert.append({currency: df.loc[df['currency'] == currency].shape[0]})
        else:
            pass

    return rows_insert


def create_tables_work(engine, stg_schema, raw_schema, file_source):
    '''
    Create tables work in DB

    Parameters
    ----------
    engine : sqlalchemy engine
        engine db
    config_aws: dict
        dict config credentials aws
    stg_schema : str
        schema db
    raw_schema : str
        schema db
    file_source: str
        name or extract of path in aws s3
    
    Returns
    ---------
    None
    '''

    query_sys = """ SELECT table_schema, table_name FROM information_schema.tables WHERE table_schema = 'DLKRAW' """
    tables = pd.read_sql_query(query_sys, con=engine)

    if 'init' in file_source:
        tables = tables.loc[tables['table_name'].str.contains('INIT')]
    elif 'increment' in file_source:
        tables = tables.loc[-tables['table_name'].str.contains('INIT')]
    else:
        pass

    conn = engine.connect()

    for index, row in tables.iterrows():

        table = row['table_name']
        query_drop = """DROP TABLE "{}"."{}_WORK" """.format(stg_schema, table)
        query_insert = """SELECT * INTO "{}"."{}_WORK" FROM "{}"."{}" """.format(stg_schema, table, raw_schema, table)
        print(query_drop)
        try:
            conn.execute(query_drop)
        except:
            pass
        print(query_insert)
        conn.execute(query_insert)

    conn.close()


