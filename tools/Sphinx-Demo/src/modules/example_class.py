#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
.. module:: example_class
   :synopsis: A useful module indeed.

'''


class Operations():
    def __init__(self, a, b):
        """
        Genera un objeto para calculos.

        Parameters
        ----------
        a : float
            Primer valor numerico.
        b: float
            Segundo valor numerico.

        """
        
        self.a = a
        self.b = b

    def suma(self):
        """
        Suma los dos atributos del objeto.

        Parameters
        ----------

        Return
        ------
        float
            Resultado de la suma de los atributos.

        """
        
        suma = self.a + self.b

        return suma


    def resta(self):
        """
        Resta los dos atributos del objeto.

        Parameters
        ----------

        Return
        ------
        float
            Resultado de la resta de los atributos.

        """
        
        resta = self.a - self.b

        return resta
