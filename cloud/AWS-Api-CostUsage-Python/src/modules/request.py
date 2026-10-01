#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import sys
import boto3
import json
import pandas as pd
from modules.log import simple_log

    
def donwload(client, start, end, folder_download, path_log, index):
    
    metric = 'BlendedCost'
    cost = [{
            'Type': 'DIMENSION',
            'Key': 'SERVICE'}]

    try:
        response = client.get_cost_and_usage(
        TimePeriod={
            'Start': start,
            'End': end
        },

        Granularity='DAILY',

        Metrics=['BlendedCost'],

        GroupBy=cost
        )
        
        response = response['ResultsByTime']

    except:
        error = sys.exc_info()
        simple_log(path_log, index, error[0], error[1])
        response = None
    
    i = 0
    list_df = []

    while True:
        try:
            df = pd.json_normalize(response[i]['Groups'])
            timestart = response[i]['TimePeriod']['Start']
            timeend = response[i]['TimePeriod']['End']
            df["Period_start"] = timestart
            df["Period_end"] = timeend

            df = df.rename(columns={'Keys': 'Service',
                                    'Metrics.BlendedCost.Amount': 'Amount',
                                    'Metrics.BlendedCost.Unit': 'CurrencyCode',})
            
            df['Amount'] = df['Amount'].astype(float)
            
            i = i + 1
            
            list_df.append(df)
            
        except IndexError:
            break
    
    try: 
        result = pd.concat(list_df)
        dic = result.to_dict(orient='records')

    except:
        error = sys.exc_info()
        simple_log(path_log, index, error[0], error[1])
        dic = None

    now = datetime.datetime.now()
    now = now.strftime('%Ya%mm%dd%Hh%Mm')
    namefile = start + '_' + now +'.json'

    jsonfile = open(folder_download + namefile, 'w')

    for row in dic:
        json.dump(row, jsonfile)
        jsonfile.write('\n')
    jsonfile.close()

    return None