#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob
import json
import time
import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from elasticsearch.helpers import bulk


def client():
    '''
    Configuracion del cliente para la cuenta Elastic
    Parameters
    ----------

    Returns
    ---------
    dict
    '''
    try:
        proes = Elasticsearch(
            ["rgioddbprd57455.dtvpan.com","rgioddbprd57456.dtvpan.com","rgioddbprd57457.dtvpan.com"],
            http_auth=("logstash", "logstash"),
            use_ssl=True
        )
    except:
        proes = None

    try:
        deves = Elasticsearch(
        host="localhost",
        port=9200,
        http_auth=None,
        use_ssl=False
        )
    except:
        deves = None

    _dict = {'pro': proes, 'dev': deves}

    return _dict


def lastupdate(client, index):
    '''
    Configuracion del cliente para la cuenta Elastic
    Parameters
    ----------
    client : elasticsearch obj
        obj con la configuracion de elasticsearch
    index: str
        indice elastic desde donde consumir los datos

    Returns
    ---------
    str
    '''
    try:
        s = Search(using=client, index=index) \
        .sort({ "Date": "desc"}) \
        .extra(size=1)

        response = s.execute()
        for hit in response:
            filename = hit.filename
    except:
        filename = None

    return filename


def insert(path, client, index):
    '''
    Funcion para desarrollo ....
    Bulk insert elastic
    
    Parameters
    ----------

    Returns
    ---------
    bool
    '''
    files = glob.glob(path+'*.json')
    files = sorted(files)

    for file in files:
        print('\n Elastic insert desde: ', file)
        df = pd.read_json(file, lines=True)
        df = df[['filename', 'lineItem/intervalUsageEnd', 'product/service']]
        df['Date'] = pd.to_datetime(df['lineItem/intervalUsageEnd'])
        df['Date'] = df['Date'].dt.strftime("%Y-%m-%dT%H:%M:%S")
        df['Date'] = pd.to_datetime(df['Date'])
        df = json.loads(df.to_json(orient='records', date_format='iso'))
        print('Numero de registros que se trataran de insertar en', index, ':',len(df))

        actions = [
            {
                "_index": index,
                "_source":i,
            }
                for i in df
            ]

        bulk(client, actions)

    return True


def esdelete(client, index, filename):
    '''
    Elimina los registros en el indice especificado en el rango de dias especificado
    '''
    try:
        s = Search(using=client, index=index) \
            .query('regexp', filename=".*{}.*".format(filename))
        response = s.delete()
        time.sleep(10)
        
        rows = s.count()
        return True
    except:
        return False


def count_rows_oci(client ,index, filename):
    '''
    Devuelve cantidad de registros del file especificado
    '''
    while True:
        s = Search(using=client, index=index) \
            .query('regexp', filename=".*{}.*".format(filename))
        rows = s.count()
        print(index, filename, rows)
        if rows == 0:
            break
        else:
            time.sleep(15)

    return rows