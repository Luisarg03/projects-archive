#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setup import dev_config, pro_config
from modules.CreateDirs import create_dir
from modules.ElasticQuery import get_client, get_time, get_id_batch, delete_rows
from modules.request import DownloadReport


if __name__ == "__main__":

    ### Desarrollo y testing
    config = dev_config

    ### Produccion
    # config = pro_config

    create_dir([config['PATH_FILES'], config['PATH_LOG']])

    es = get_client(config['HOST'], config['USER'], config['PASS'])
    date = get_time(es, config['INDEX_SOURCE'])

    # Descomentar y setear la fecha a reprocesar
    date = '2020-05'

    id_batch = get_id_batch(es, config['INDEX_SOURCE'], config['PATH_LOG'])
    delete_rows(es, config['INDEX_SOURCE'], date, config['PATH_LOG'], id_batch)

    DownloadReport(config['ACCOUNT'],
                   config['APIKEY'],
                   date, # Fecha que se descargara
                   config['PATH_FILES'],
                   id_batch,
                   config['INDEX_SOURCE'],
                   config['PATH_LOG'])
