from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from . import db


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(50), unique=True, nullable=False)

    email = db.Column(db.String(90), unique=True, nullable=False)

    password_encryp = db.Column(db.String(93), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.now())
    # Relaciono mi modelo User con el de Task
    tasks = db.relationship('Task', lazy='dynamic')

    # verifico el pass que me manda el usuario
    # check_password devuelve True si ambas pass coinciden
    def verify_password(self, password):
        return check_password_hash(self.password_encryp, password)

    @property
    def password(self):
        pass

    @password.setter
    def password(self, value):
        self.password_encryp = generate_password_hash(value)

    def __str__(self):
        return self.username

    @classmethod
    def create_element(cls, username, email, password):
        user = User(username=username, email=email, password=password)

        db.session.add(user)
        db.session.commit()

        return user

    # filtro para obtener usuarios, emails e ids
    # Obtendre usuario ya registrados
    @classmethod
    def get_user(cls, username):
        return User.query.filter_by(username=username).first()

    @classmethod
    def get_email(cls, email):
        return User.query.filter_by(email=email).first()

    @classmethod
    def get_by_id(cls, id):
        return User.query.filter_by(id=id).first()


class Task(db.Model):

    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.Text())
    # Indico que la relacion va a ser de uno a muchos
    # Un usuario puede tener muchas tareas
    # Las tareas son de un solo usuario
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.now())

    # Abrevia la descripcion que aparece en el la lista de tareas
    @property
    def little_descrip(self):
        if len(self.description) > 25:
            return self.description[0:24] + '...'
        else:
            return self.description

    # Acorto los datos que aparecen en la fecha
    @property
    def little_at(self):
        now = str(self.created_at)
        return now[0:16] + ' hs'

    @classmethod
    def create_element(cls, title, description, user_id):
        task = Task(title=title, description=description, user_id=user_id)

        db.session.add(task)
        db.session.commit()

        return task

    @classmethod
    def get_by_id(cls, id):
        return Task.query.filter_by(id=id).first()

    @classmethod
    def update_element(cls, id, title, description):
        task = Task.get_by_id(id)

        if task is None:
            return False
        else:
            task.title = title
            task.description = description

            db.session.add(task)
            db.session.commit()

        return task

    @classmethod
    def delete_element(cls, id):
        task = Task.get_by_id(id)

        if task is None:
            return False
        else:
            db.session.delete(task)
            db.session.commit()

        return True
