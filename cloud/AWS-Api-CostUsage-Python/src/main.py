#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import pandas as pd
from modules.CreateDirs import create_dir
from modules.request import donwload
from modules.GetTime import time_range
from modules.ElasticQuery import get_client, delete_rows
from config import config_user


if __name__ == "__main__":

    config = config_user()
    
    create_dir([
        config['PATH_RG'],
        config['PATH_EC'],
        config['PATH_LOG'],
        ])

    client = get_client(config['HOST'], config['USER'], config['PASS'])

    time_rg = time_range(client, config['INDEX'][0], config['PATH_LOG'])
    time_ec = time_range(client, config['INDEX'][1], config['PATH_LOG'])

    if time_rg is None:
        pass
    else:
        delete_rows(client, config['INDEX'][0], time_rg['start'], config['PATH_LOG'])
        donwload(config['CLIENT_RG'], time_rg['start'], time_rg['end'], config['PATH_RG'], config['PATH_LOG'], config['INDEX'][0])

    if time_ec is None:
        pass
    else:
        delete_rows(client, config['INDEX'][1], time_rg['start'], config['PATH_LOG'])
        donwload(config['CLIENT_EC'], time_ec['start'], time_ec['end'], config['PATH_EC'], config['PATH_LOG'], config['INDEX'][1])