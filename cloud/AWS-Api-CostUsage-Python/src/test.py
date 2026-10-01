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

    start = '2020-04-01'
    end = '2020-04-02'

    donwload(config['CLIENT_RG'], start, end, config['PATH_RG'], config['PATH_LOG'], 'rg')
    donwload(config['CLIENT_EC'], start, end, config['PATH_EC'], config['PATH_LOG'], 'ec')