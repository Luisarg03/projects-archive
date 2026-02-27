#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import pandas as pd
import numpy as np
from sqlalchemy import types

def clear_duplicated(engine, schema, file_source):
    '''
    run query to delete duplicates

    Parameters
    ----------
    engine : sqlalchemy engine
        engine db
    schema : str
        schema db
    file_source: str
        name or extract of path in aws s3
    
    Returns
    ---------
    None
    '''

    query_sys = """ SELECT table_schema, table_name FROM information_schema.tables WHERE table_schema = '{}' """.format(schema)
    tables = pd.read_sql_query(query_sys, con=engine)

    # Filter tables to use in db
    if 'init' in file_source:
        tables = tables.loc[tables['table_name'].str.contains('INIT')]
    elif 'increment' in file_source:
        tables = tables.loc[-tables['table_name'].str.contains('INIT')]
    else:
        pass

    conn = engine.connect()

    for index, row in tables.iterrows():

        table = row['table_name']
        query_delete = """
                        DELETE FROM "{}"."{}"
                        WHERE ctid IN (
                        SELECT unnest(array_remove(all_ctids, actid))
                        FROM (
                                SELECT
                                min(b.ctid)     AS actid,
                                array_agg(ctid) AS all_ctids
                                FROM "{}"."{}" b
                                GROUP BY id
                                HAVING count(*) > 1) c) 
                        """.format(schema, table, schema, table)
            
        print(query_delete)
        conn.execute(query_delete)
    
    conn.close()


def create_fct_table(engine, stg_schema, cur_schema, file_source):
    '''
    Normalize data and create stg_fct_table

    Parameters
    ----------
    engine : sqlalchemy engine
        engine db
    stg_schema : str
        schema db
    cur_schema : str
        schema db
    file_source: str
        name or extract of path in aws s3
    
    Returns
    ---------
    None
    '''

    name_table = "FCT_SALES"
    query_sys = """ SELECT table_schema, table_name FROM information_schema.tables WHERE table_schema = '{}' """.format(stg_schema)

    tables = pd.read_sql_query(query_sys, con=engine)

    # Filter tables to use in db
    if 'init' in file_source:
        tables = tables.loc[tables['table_name'].str.contains('INIT')]
    elif 'increment' in file_source:
        tables = tables.loc[-tables['table_name'].str.contains('INIT')]
    else:
        pass

    for index, row in tables.iterrows():
        query = "".join(["SELECT * FROM ", '"',row['table_schema'],'"','."',row['table_name'],'"'])
        print(query)
        
        for df in pd.read_sql_query(query, con=engine, chunksize=20000):

            # Set cols best type Datetime -> infer_datetime_format=True 
            df['updated_date'] = pd.to_datetime(df['updated_date'], infer_datetime_format=True)
            df['created_date'] = pd.to_datetime(df['created_date'], infer_datetime_format=True)

            # Set cols min type length INT -> downcast='integer'
            df['year'], df['month'], df['day'] =  df['updated_date'].apply(lambda x: x.year), \
                                                df['updated_date'].apply(lambda x: x.month), \
                                                df['updated_date'].apply(lambda x: x.day)
            
            cols_date = ['year', 'month', 'day']
            for col in cols_date:
                df[col] = pd.to_numeric(df[col], downcast='integer')
            
            # Rule of Challenge -> Create "product_type" col and filters
            df['product_type'] = df['subtitle']
            filter = {
                'Coca cola sin azúcar': ['Coca-Cola Sin Azúcar Retornable',
                                    'COCA-COLA SIN AZÚCAR SIN AZÚCARES',
                                    'Bebida Coca-Cola Sin Azúcar Mediana',
                                    'COCA-COLA SIN AZÚCARES',
                                    'Coca-Cola Sin Azúcar'],
                'Coca cola original': ['Coca-Cola Original',
                                    'Bebida sin Alcohol Coca-Cola Sabor Original',
                                    'Coca-Cola SABOR ORIGINAL',
                                    'COCA-COLA SABOR ORIGINAL SABOR ORIGINAL',
                                    'Bebida Coca Cola Sabor Original']}

            for key, values in zip(filter.keys(), filter.values()):
                for value in values:
                    df['product_type'].loc[df['product_type'] == value] = key.upper()

            df['product_type'].loc[ \
                                (df['product_type'] != 'Coca cola sin azúcar'.upper()) & \
                                (df['product_type'] != 'Coca cola original'.upper())] = 'OTHER'
            
            # Convert cols with numbers (for agg) to float
            cols_num = ['amount', 'quantity', 'units', 'retail_amount']
            for col in cols_num:
                p = re.compile(r'(^[0-9]*[.,]{0,1}[0-9]*$)')
                df[col] = df[col].str.extract(p, expand=False)
                df[col] = pd.to_numeric(df[col], downcast='float')

            # Set cols type sqlalchemy
            dtypes = {}
            for i in df.dtypes.unique():
                for k in df.columns[df.dtypes == i].tolist():
                    if 'obj' in str(i):
                        dtypes[k] = types.VARCHAR(length=350)
                    elif 'float' in str(i):
                        dtypes[k] = types.Float
                    elif 'int' in str(i):
                        dtypes[k] = types.Integer
                    elif 'datetime' in str(i):
                        dtypes[k] = types.Date
                    else:
                        pass
            
            ### Replace NaN values
            for i in df.dtypes.unique():
                for k in df.columns[df.dtypes == i].tolist():
                    if 'obj' in str(i):
                        df[k] = df[k].replace('nan', np.NaN)
                        df[k] = df[k].fillna('NoDefine')
                    elif 'float' in str(i):
                        df[k] = df[k].fillna(0)
                    elif 'int' in str(i):
                        df[k] = df[k].fillna(0)
                    else:
                        pass
            
            ### Condition source and create normalized table
            if 'init' in file_source:
                df.to_sql(name=name_table+'_INIT', con=engine, schema=cur_schema, if_exists='append', index=False, dtype=dtypes)
            elif 'increment' in file_source:
                df.to_sql(name=name_table+'_INCREMENT', con=engine, schema=cur_schema, if_exists='append', index=False, dtype=dtypes)


def create_dim(engine, schema, file_source):
    '''
    Create dim tables

    Parameters
    ----------
    engine : sqlalchemy engine
        engine db
    schema : str
        schema db
    file_source: str
        name or extract of path in aws s3
    
    Returns
    ---------
    None
    '''

    query_sys = """ SELECT table_schema, table_name FROM information_schema.tables WHERE table_schema = '{}' """.format(schema)
    tables = pd.read_sql_query(query_sys, con=engine)

    # Filter tables to use in db
    if 'init' in file_source:
        tables = tables.loc[tables['table_name'].str.contains('INIT')]
    elif 'increment' in file_source:
        tables = tables.loc[-tables['table_name'].str.contains('INIT')]
    else:
        pass
    
    split_tables = {
    'CATEGORY': ['category_code', 'category_name', 'category_color'], 
    'MANUFACTER': ['manufacturer_id', 'manufacturer_name'],
    'PRODUCT': ['sku', 'units', 'product_type', 'title', 'subtitle', 'details', 'ean', 'brand', 'flavor', 'variant', 'category_code']
               }

    for index, row in tables.iterrows():
        query = "".join(["SELECT * FROM ", '"',row['table_schema'],'"','."',row['table_name'],'"'])
        
        for df in pd.read_sql_query(query, con=engine, chunksize=20000):
            if 'FCT_SALES_INIT' in query:
                for i, k in zip(split_tables.keys(), split_tables.values()):
                    table_name = 'DIM_'+i+'_INIT'

                    df[k].drop_duplicates(). \
                    to_sql(name=table_name, con=engine, schema=schema, if_exists='append', index=False)

            elif 'FCT_SALES_INCREMENT' in query:
                for i, k in zip(split_tables.keys(), split_tables.values()):
                    table_name = 'DIM_'+i+'_INCREMENT'

                    df[k].drop_duplicates(). \
                    to_sql(name=table_name, con=engine, schema=schema, if_exists='append', index=False)
            else:
                pass