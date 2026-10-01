#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import sys
import json


def simple_log(path_log, index, id, method, type, value):
    now = datetime.datetime.now()
    now = now.strftime('%Ya%mm%dd%Hh%Mm')
    error = sys.exc_info()

    with open(path_log+ 'Error_' + index + '_' + now + '.log', 'a+') as f:
        dict_log = {
            'index': index,
            'method': method,
            'id_batch': id,
            'type': str(type),
            'value': str(value),
            'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        }

        f.write(json.dumps(dict_log))
        f.close()