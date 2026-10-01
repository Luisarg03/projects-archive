#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
import boto3

def config_user():

    PATH_DOWNLOAD = '../JsonReports/'

    config = dict(

        PATH_RG = PATH_DOWNLOAD+'CostReg/',
        PATH_EC = PATH_DOWNLOAD+'CostEcu/',
        PATH_LOG = '../LogErros/',

        ### Credendiales HOST
        HOST = [],
        USER = None,
        PASS = None,
        INDEX = [],

        ### Credenciales de usuario1
        CLIENT_RG = boto3.client('ce',
                                aws_access_key_id=None,
                                aws_secret_access_key=None),

        ### Credenciales de usuario2
        CLIENT_EC = boto3.client('ce',
                                aws_access_key_id=None,
                                aws_secret_access_key=None),
    )

    return config