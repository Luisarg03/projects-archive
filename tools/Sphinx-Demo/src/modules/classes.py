#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
.. module:: classes
   :synopsis: A useful module indeed.

'''


class Connect():
    '''
    Genera una conexion al bucket definido.

    '''

    def __init__(self, namespace, bucket_name):
        '''
        Genera una conexion al bucket definido.

        Parameters
        ----------
        namespace : str
            NameSpace de su ObjectStorage Service
        bucket_name: str
            Alias asignado a su ObjectStorage Service

        '''
        
        self.namespace = namespace
        self.bucket_name = bucket_name


    def ping(self, retry=1):
        '''
        Prueba de conexion.

        Parameters
        ----------
        retry: int
            Numero de intentos de reconexion (default 1)

        Return
        ------
        float
            Valor numerico que representa el ping de conexion.
        '''
        
        ping = 0.9

        return ping
