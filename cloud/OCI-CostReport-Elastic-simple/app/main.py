#!/usr/bin/env python
# -*- coding: utf-8 -*-
from modules.client import get_client
from modules.ElasticQuery import client, esdelete, count_rows_oci
from modules.Unzip import create_paths, unzip_list
from modules.request import RequestDownload
from modules.PandasProcess import PreProcess

from modules.ElasticQuery import insert ### Dev funtion

import pandas as pd
import numpy as np

### Configuracion cliente OCI
config = '../OciConfig/config.prod'
account = 'DC'
ociclient = get_client(config, account)


### Configuracion cliente elastic
esclient = client()
print('\n clientes elastic: ', esclient)


### Variables para desarrollo
# index = "oci-dev"
# esclient = esclient['dev']


### Variables productivas
index = "oci-dc"
esclient = esclient['pro']


if __name__ == '__main__':

    path = create_paths()

    _dir = '/home/luis/desarrollo/tsoft/metadata/Metadata/reproceso.csv'
    df = pd.read_csv(_dir, dtype={'filename': np.str_})

    for file in df['filename']:
        prefix = "reports/cost-csv/"+file
        print(prefix)

        file = int(file)
        esdelete(esclient, index, file)
        count_rows_oci(esclient, index, file)

        ## Descarga de los nuevos files
        list_files = RequestDownload(
            ociclient['client'],
            ociclient['bucket'],
            prefix,
            path
            )

        unzip_list(path, list_files)
        PreProcess(path, list_files)


    # # ## Desa funcion
    # insert(path, esclient, index)
