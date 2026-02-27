#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import sys
import json

def simple_log(path_log, index, type, value):
    now = datetime.datetime.now()
    now = now.strftime('%Ya%mm%dd%Hh%Mm')
    error = sys.exc_info()

    with open(path_log+ 'Error_' + index + '_' + now + '.log', 'a+') as f:
        dict_log = {
            'type': str(type),
            'value': str(value),
        }

        f.write(json.dumps(dict_log))
        f.close()