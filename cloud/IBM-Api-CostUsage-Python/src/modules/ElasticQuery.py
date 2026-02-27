#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys
import datetime
import pandas as pd
from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Search
from modules.log import simple_log


def get_client(host, user, key):
    ### Cliente Sv
    client = Elasticsearch(host, http_auth=(user, key), use_ssl=True)
    
    return client


def get_time(client, index):

    start = datetime.datetime.now()
    start = start.strftime("%Y-%m")

    return start


def get_id_batch(client, index, path_log):
    name = __name__+'.get_id_batch'
    try:
        s = Search(using=client, index=index) \
            .query('range' ,  **{'Date': {'gte': "now-7d/d"}}) \
            .sort({"BatchID" : {"order" : "desc"}}) \
            .query("match_all")

        for hit in s[0]:
            last_batch = hit.BatchID

    except:
        last_batch = None
        error = sys.exc_info()
        simple_log(path_log, index, last_batch, name, error[0], error[1])

    return last_batch


def delete_rows(client, index, date, path_log, id):
    name = __name__+'.delete_rows'
    try:
        s = Search(using=client, index=index) \
        .filter('range' ,  **{'Date': {'gte': date, "lte": date}})
        response = s.delete()
    except:
        error = sys.exc_info()
        simple_log(path_log, index, id, name, error[0], error[1])

    return None