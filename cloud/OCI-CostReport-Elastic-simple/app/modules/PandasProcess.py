#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import re
import os
import glob
import json
import shutil


def PreProcess(path, filename):
    '''
    Lee todos los .csv del directorio y los convierte a .json
    Parameters
    ----------
    path : str
        path donde se encuentran los files descargados
    filename: list
        lista de path de files descargados

    Returns
    ---------
    bool
    '''
    paths = glob.glob(path+'*.csv')

    for file in paths:
        print('conviertiendo: ', file)
        matching = [s for s in filename if file[18:-6] in s]
            
        df = pd.read_csv(file, low_memory=False)
        df = df.fillna('null')

        df['filename'] = matching[0]

        dic = df.to_dict(orient='records')
        id = file[14:-4]

        # Crea el .json donde se guarda la data particionada
        jsonfile = open(path+id+'.json', 'w')
        print('escribiendo: ', jsonfile)
        for row in dic:
            json.dump(row, jsonfile)
            jsonfile.write('\n')

        del df
        del dic
        os.remove(file)

        folder = '../report/'
        shutil.move(path+id+'.json', folder)

    return True
