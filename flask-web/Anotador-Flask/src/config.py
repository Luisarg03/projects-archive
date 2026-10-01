from app.constan import const
import os


# Almacena la configuracion global en el servidor
class Config():
    SECRET_KEY = const.password  # genera token CSRF


# Configuraciones para el entorno de desarrollo
class DevelopmentConfig(Config):
    # Crea la BD en la ruta del proyecto
    dbdir = 'sqlite:///'+os.path.abspath(os.getcwd())+'/flask.db'
    ''' dbdir = "mysql+pymysql://Luis03:Luis03.mysql.pythonanywhere-services.com/Luis03$flask'''

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = dbdir
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuración para correos
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = const.email
    MAIL_PASSWORD = const.password


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
