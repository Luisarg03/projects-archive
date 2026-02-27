#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(port=32000, debug=True)  # Levanto mi servidor Desa