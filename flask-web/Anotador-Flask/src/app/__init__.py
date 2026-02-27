# Convierto mi carpeta app en un modulo
# Importo Bootstrap a mi proyecto
# Proteccion de formularios
# importo el archivo con su intancia
from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
# Creo mi instancia de Flask
app = Flask(__name__)
# Creo la instancia de mis herramientas
mail = Mail()
bootstrap = Bootstrap()
csrf = CSRFProtect()
login_manage = LoginManager()
db = SQLAlchemy()

# importo mi instancia Blueprint
from .views import page


# Una funcion que solo retorna mi objeto app
# Le indico que use las configuraciones de mis clases
def create_app(config):
    app.config.from_object(config)  # Argumento -> objeto
    bootstrap.init_app(app)  # Implemento boots a mi app
    csrf.init_app(app)  # generador de tokens,necesito una key
    mail.init_app(app)
    app.register_blueprint(page)  # importa las rutas a usar
    login_manage.init_app(app)
    login_manage.login_view = '.login'  # url_for
    login_manage.login_message = 'Es necesario iniciar session'
    login_manage.login_message_category = 'error'

    with app.app_context():
        db.init_app(app)
        db.create_all()  # Genero mis modelos de tablas

    return app
# Esta funcion se exportara hacia manage.py
