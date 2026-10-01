from flask import Flask
from .views import page
from .data_source.request import my_data
from .data_source.snapshot import arg_stats, snap_top
from .data_plot.plot_data import plot_arg, plot_top

app = Flask(__name__)
data_general = my_data()
var_arg = arg_stats(data_general)
data_arg = var_arg[0]
snap_top = snap_top(data_general)
data_top = snap_top[0]
ds1 = snap_top[1]
ds2 = snap_top[2]
ds3 = snap_top[3]


def create_app():
    plot_arg(data_arg)
    plot_top(data_top, ds1, ds2, ds3)
    app.register_blueprint(page)  # importa las rutas a usar

    return app
