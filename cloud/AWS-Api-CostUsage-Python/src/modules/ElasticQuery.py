#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Search
from modules.log import simple_log


def get_client(host, user, key):
    client = Elasticsearch(host, http_auth=(user, key), use_ssl=True)
    return client


def delete_rows(client, index, date, path_log):
    try:
        s = Search(using=client, index=index) \
        .filter('range' ,  **{'Date': {'gte': date, "lte": date}})
        response = s.delete()
    except:
        error = sys.exc_info()
        simple_log(path_log, index, error[0], error[1])

    return None