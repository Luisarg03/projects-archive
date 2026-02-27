
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from wtforms import Form, validators
from wtforms import StringField, PasswordField, BooleanField, TextAreaField


class ConnectForm(Form):
        host = StringField('', [
            validators.InputRequired(message='Debes ingresar host')
        ])

        user = StringField('', [
            validators.InputRequired(message='Debes ingresar usuario')
        ])

        key = PasswordField('', [
            validators.InputRequired(message='Debes ingresar una clave')
        ])

        index = StringField('', [
            validators.InputRequired(message='Debes ingresar un nombre de indice')
        ])