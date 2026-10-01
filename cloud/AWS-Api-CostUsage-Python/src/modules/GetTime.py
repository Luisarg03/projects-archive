#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import sys
import json
from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Search
from modules.log import simple_log


def time_range(client, index, path_log):
    ### Cliente Sv
    try:
        s = Search(using=client, index=index) \
            .query('range' ,  **{'Date': {'gte': "now-7d/d"}}) \
            .sort({"Date" : {"order" : "desc"}}) \
            .query("match_all")

        for hit in s[0]:
            print(hit.Date)
            last_update = hit.Date

        start = datetime.datetime.strptime(last_update.strip(), "%Y-%m-%dT%H:%M:%S.%fZ")
        start = start + datetime.timedelta(days=1)
        end = start + datetime.timedelta(days=1)

        start = start.strftime("%Y-%m-%d")
        end = end.strftime("%Y-%m-%d")

        time_dict = {
            "start": start,
            "end": end
        }
    
    except:
        error = sys.exc_info()
        simple_log(path_log, index, error[0], error[1])
        time_dict = None

    return time_dict