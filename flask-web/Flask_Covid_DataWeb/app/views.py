from flask import Blueprint, render_template, Response
from .data_source.request import my_data
from .data_source.snapshot import snap_top, arg_stats

# instancia de blueprint
page = Blueprint('page', __name__)

data_general = my_data()
data = snap_top(data_general)
df = data[4]
df_top = data[0]
val_arg = arg_stats(data_general)
md_data = val_arg[1:]


@page.route('/')
def index():

    return render_template('index.html',
                           tables=df.values)


@page.route('/arg')
def arg():

    return render_template('arg.html', dato=md_data)


@page.route('/rank')
def rank():

    return render_template('rank.html', tables=df_top.values)


@page.route('/data_to_csv')
def export():
    csv = df.to_csv(index=False)

    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=DataCovid.csv"})