#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
.. module:: functions
   :synopsis: A useful module indeed.

'''


def connect(namespace, bucket_name): 
        """
        Genera una conexion al bucket definido.

        Parameters
        ----------
        namespace : str
            NameSpace de su ObjectStorage Service
        bucket_name: str
            Alias asignado a su ObjectStorage Service

        Return
        ------
        str
            Returna un mensaje
        """

        message = 'successful connection'
        
        return message