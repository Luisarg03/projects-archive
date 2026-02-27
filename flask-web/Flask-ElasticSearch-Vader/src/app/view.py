#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from flask import Blueprint, render_template, request, session
from flask import redirect, url_for, flash
from .forms import ConnectForm
from .querys import ElasticConnect
from .etl import TransformData


page = Blueprint('page', __name__)

@page.route('/', methods=['POST', 'GET'])
def index():
    form_from = ConnectForm(request.form)

    if request.method == 'POST' and form_from.validate():

        data_from = ElasticConnect(
            form_from.host.data,
            form_from.user.data,
            form_from.key.data,
            form_from.index.data)

        data_dic = data_from.get_client()
        columns = data_from.get_columns()

        if 1 in columns or 2 in columns:
            flash(columns[0], 'error')
            return render_template('index.html', form=form_from)
        
        session['data_from'] = data_dic
        session['index_from'] = form_from.index.data
        session['columns_from'] = columns

        return redirect(url_for('.form_to'))

    return render_template('index.html', form=form_from)


@page.route('/form_to', methods=['POST', 'GET'])
def form_to():
    index_name_from = session.get('index_from', None)
    columns_from = session.get('columns_from', None)

    form_to = ConnectForm(request.form)

    if request.method == 'POST' and form_to.validate() and request.form['submit_button'] == 'confirm':

        select_field_message = request.form.get('field_select_message')
        select_field_date = request.form.get('field_select_date')

        conection = ElasticConnect(
            form_to.host.data,
            form_to.user.data,
            form_to.key.data,
            form_to.index.data)
        
        test_connect = conection.test_connect()

        if test_connect == True:
            data_to = conection.get_client()
            session['data_to'] = data_to
            session['select_field_message'] = select_field_message
            session['select_field_date'] = select_field_date

            return redirect(url_for('.confirm'))
        else:
            flash(test_connect[0], 'error')
            flash('HOST, USER, KEY', 'error')
            return redirect(url_for('.form_to'))
    
    elif request.method == 'POST' and request.form['submit_button'] == 'return':
        return redirect(url_for('.index'))

    return render_template('form_to.html',
                            columns=columns_from,
                            index=index_name_from,
                            form=form_to)


@page.route('/confirm', methods=['POST', 'GET'])
def confirm():

    data_from = session.get('data_from', None)
    data_to = session.get('data_to', None)
    select_field_message = session.get('select_field_message', None)
    select_field_date = session.get('select_field_date', None)

    if request.method == 'POST':
        if request.form['submit_button'] == 'confirm':
            return redirect(url_for('.active_service'))

        elif request.form['submit_button'] == 'return':
            return redirect(url_for('.form_to'))

    return render_template('confirm.html',
                            data_from=data_from,
                            data_to=data_to,
                            field_message=select_field_message,
                            field_date=select_field_date)


@page.route('/active_service', methods=['POST', 'GET'])
def active_service():

    if request.method == 'POST':
        return test()
    
    return render_template('active_service.html')


def test():
    data_from = session.get('data_from', None)
    data_to = session.get('data_to', None)
    field_messages = session.get('select_field_message', None)
    date = session.get('select_field_date', None)

    while True:
        conection_from = ElasticConnect(
            data_from['host'],
            data_from['user'],
            data_from['key'],
            data_from['index'])

        conection_to = ElasticConnect(
            data_to['host'],
            data_to['user'],
            data_to['key'],
            data_to['index'])

        test_connect_from = conection_from.test_connect()
        update = conection_from.get_range_time(date)
        data = conection_from.get_data(date, field_messages, update)

        test_connect_to = conection_to.test_connect()

        if test_connect_to == True:
            data = TransformData(data, field_messages)
            data = data.get_sentiments()
            conection_to.create_insert(data, conection_to.index)
        
        time.sleep(1200) ### reload process


# Funcion que se activa a travez de un error
@page.app_errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404
# el segundo valor es convencion para notificar el error