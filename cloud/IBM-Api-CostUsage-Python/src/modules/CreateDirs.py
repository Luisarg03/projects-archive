#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import shutil


def create_dir(paths):

    for i in paths:
        if os.path.exists(i):
            shutil.rmtree(i)
            os.makedirs(i)
                
        if not os.path.exists(i):
            os.makedirs(i)

        else:
            pass