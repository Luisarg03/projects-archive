# Importo manager que me permite levantar el servidor
# a partir de una instancia
# Importo mi instancia 'app'
# Importo mi diccionario con las clases que tiene dentro
from flask_script import Manager
from app import create_app
from config import config

# mi diccionario con las configuraciones
config_class = config['development']
# Se importa la instancia y obtengo mi aplicación
app = create_app(config_class)

if __name__ == '__main__':
    manager = Manager(app)  # paso como argumento mi app
    manager.run()  # Levanto mi servidor
