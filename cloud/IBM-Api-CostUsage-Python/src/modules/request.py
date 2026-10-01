#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import requests
import json
import datetime
import pandas as pd
from modules.log import simple_log


def get_token(apikey):
    name = __name__+'.get_token'
    try:
        url = "https://iam.cloud.ibm.com/identity/token?grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey="
        payload = {}
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        }

        response = requests.request("POST", url+apikey, headers=headers, data=payload)

        data = json.loads(response.text)

        token = data['access_token']

    except:
        error = sys.exc_info()
        simple_log(path_log, index, name, error[0], error[1])
        token = None

    return token


def processResourceInstanceUsage(account_id, billMonth, iam_token, offset):
    name = __name__+'.processResourceInstanceUsage'
    try:
        METERING_HOST = "https://billing.cloud.ibm.com"

        USAGE_URL = "/v4/accounts/"+account_id+"/resource_instances/usage/"+billMonth+"?_limit=200&_names=true&_start="+offset

        url = METERING_HOST+USAGE_URL

        headers = {
            "Authorization": "{}".format(iam_token),
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        response = requests.get(url, headers=headers)
        response = response.json()

    except:
        error = sys.exc_info()
        simple_log(path_log, index, name, error[0], error[1])
        response = None

    return response


def concatdata(account, billMonth, token, offset):
    response_data = []

    while True:
        try:
            response_json = processResourceInstanceUsage(account, billMonth, token, offset)
            offset = response_json['next']['offset']

            response_data.append(response_json['resources'])

        except KeyError:
            try:
                response_data.append(response_json['resources'])
            except:
                break

            break

    return response_data


def pandasnorm(response_data):
    name = __name__+'.pandasnorm'
    list_df = []

    fileds = ['account_id', 'resource_instance_id', 'resource_group_id', 'month',
           'pricing_country', 'billing_country', 'currency_code', 'plan_id',
           'resource_id', 'billable', 'pricing_plan_id',
           'region', 'usage', 'plan_name', 'resource_name',
           'resource_instance_name', 'resource_group_name']

    try:
        for i in response_data:

            df = pd.json_normalize(i, 'usage', fileds)

            for k in ['price', 'break_down', 'discounts', 'usage']:
                try:
                    df = df.drop(k, axis=1)
                except:
                    pass

            list_df.append(df)

        result = pd.concat(list_df)

    except:
        error = sys.exc_info()
        simple_log(path_log, index, name, error[0], error[1])
        result = None

    return result


def DownloadReport(account, apikey, date, path, batch, index, path_log):
    name = __name__+'.DownloadReport'
    token = get_token(apikey)
    billMonth = date
    offset = ''
    data = concatdata(account, billMonth, token, offset)
    df = pandasnorm(data)

    try:
        # df['BatchID'] = batch
        dic = df.to_dict(orient='records')

        now = datetime.datetime.now().strftime('%Yy%mm%dd%Hh%Mm')
        name_file = path+'DataIBM_'+ now + '.json'
        jsonfile = open(name_file, 'w')

        for row in dic:
            json.dump(row, jsonfile)
            jsonfile.write('\n')
        jsonfile.close()

    except:
        error = sys.exc_info()
        simple_log(path_log, index, batch, name, error[0], error[1])

    return None