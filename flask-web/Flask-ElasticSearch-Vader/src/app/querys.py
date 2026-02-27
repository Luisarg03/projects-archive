#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import json
from elasticsearch import Elasticsearch, helpers, exceptions
from elasticsearch_dsl import Search


class ElasticConnect():
    def __init__(self, host, user: str, key: str, index: str):
        try:
            self.host = list(host.replace(',', '').split())
        except AttributeError:
            self.host = host

        self.user = user.strip()
        self.key = key.strip()
        self.index = index.strip()
        self.client = Elasticsearch(self.host, http_auth=(self.user, self.key), use_ssl=False)


    def get_client(self):
        data_dic = {
            'host': self.host,
            'user': self.user,
            'key': self.key,
            'index': self.index,
        }

        return data_dic


    def test_connect(self):
        if not self.client.ping():
            error = 'Error de conexion con ElasticSearch'
            return [error, 1]
        else:
            return True


    def get_columns(self):
        try:
            # SET use_ssl=True IN ENV PRO
            # TEST http_auth IN ENV PRO
            s = Search(using=self.client, index=self.index)
            df = pd.DataFrame((d.to_dict() for d in s[1]))
            df = df.select_dtypes(include=["O"])
            df = list(df.columns)

        except exceptions.ConnectionError:
            error = 'Error de conexion con ElasticSearch'
            return [error, 1]
        
        except exceptions.NotFoundError:
            error = 'Error de indice inexistente'
            return [error, 2]

        return df

    
    def get_range_time(self, column_date):
        try:
            s = Search(using=self.client, index=self.index) \
            .sort({column_date: {"order" : "desc"}}) \
            .query("match_all")

            df = pd.DataFrame((d.to_dict() for d in s[0:5].scan()))
            df = df[df[column_date] == df[column_date].max()]
            df[column_date] = pd.to_datetime(df[column_date])
            df[column_date] = df[column_date].dt.strftime("%Y-%m-%dT%H:%M:%S")
            time = df[column_date].iloc[0] # ej: 2021-03-17T19:57:36
        except:
            time = None

        return time
    

    def get_data(self, column_date, column_message, time):

        # s = Search(using=self.client, index=self.index) \
        # .query('range' , **{column_date: {'gt': None}}) ## Change None for 'time' (var)

        s = Search(using=self.client, index=self.index)
        df = pd.DataFrame((d.to_dict() for d in s.scan()))
        df['from_index'] = self.index
        df = df[['from_index', column_date, column_message]]
        df = df.dropna(subset=[column_message])
        df = df.drop_duplicates(subset=[column_message])

        return df

    
    def create_insert(self, df, index):
        df = json.loads(df.to_json(orient='records', date_format='iso'))

        actions = [
        {
            "_index": index,
            "_source":i,

        }
            for i in df
        ]

        helpers.bulk(self.client, actions)

        return True